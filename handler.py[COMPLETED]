import sys
import os
import hashlib


class File:
    def __init__(self, name_of, path_to, size_of, type_of, hash_of):
        self.name = name_of
        self.path = path_to
        self.size = size_of
        self.type = type_of[1:]  # removing dot from extension name
        self.hash = hash_of.hexdigest()  # hash in form: 909ba4ad2bda46b10aac3c5b7f01abd5
        self.id = None

    def __str__(self):
        return f"{self.path}"


def sorter(list_of_objects, order):
    """Sorting passed list of files or folders by its size"""
    if order == '1':  # descending
        return sorted(list_of_objects, key=lambda x: -x.size)
    elif order == '2':  # ascending
        return sorted(list_of_objects, key=lambda x: x.size)


def delete_files(files_to_delete):
    """Deletes files by file.id. Takes list with id's as input. Count size of deleted files."""
    counter = 0
    for size, hashes in files_with_same_hashes.items():
            for hash_, files in hashes.items():
                if len(files) > 1:
                    for file in files:
                        if file.id in files_to_delete:
                            os.remove(file.path)
                            counter += file.size
    return counter


all_files = []
files_sizes = []
files_hashes = []
files_with_same_hashes = {}
files_with_same_sizes = {}

try:
    root_path = sys.argv[1]  # reading command line argument [0] its script file itself, [1] - its path to root folder
    if os.path.isdir(root_path) or os.path.isfile(root_path):
        for root, dirs, files in os.walk(root_path):
            for name in files:
                hash_of_file = hashlib.md5()
                path_to_file = os.path.join(root, name)  # building path to file: root\folder\file_name.extension
                object_size = os.path.getsize(path_to_file)  # size of file in bytes
                object_head, object_type = os.path.splitext(path_to_file)  # object_head = file, object_type = .extension
                with open(path_to_file, 'rb') as f:  # reading file in binary mode
                    hash_of_file.update(f.read())  # creating md5 hash of file
                all_files.append(File(name, path_to_file,  # creating list of objects Class File
                                      object_size, object_type,
                                      hash_of_file))
except IndexError:
    print("Directory is not specified")

requested_ext = input("Enter file format:").strip().lower()
option = None

while True:
    print("Size sorting options:\n1. Descending\n2. Ascending")
    option = input("Enter a sorting option:\n")
    if option in ['1', '2']:
        break
    else:
        print("Wrong option")


all_files = sorter(all_files, option)  # sort files in provided order

for file in all_files:  # creating list of different sizes and hashes of objects
    if file.size not in files_sizes:
        files_sizes.append(file.size)
    if file.hash not in files_hashes:
        files_hashes.append(file.hash)

files_with_same_sizes = {size: [file for file in all_files  # dict of files with same sizes and provided extension
                                if file.size == size        # structure: key = size, value = [files with that size]
                                and (file.type == requested_ext
                                     or requested_ext == '')]
                         for size in files_sizes}

for size, files in files_with_same_sizes.items():
    print(f"\n{size} bytes")
    for file in files:
        print(file)

n = 1
while True:
    print("\nCheck for duplicates? yes\\no")
    duplicates = input()
    if duplicates == 'yes':
        files_with_same_hashes = {size: {hash_: [file for file in all_files  # dict of files with same size, hash and
                                                 if file.hash == hash_       # provided extension
                                                 and file.size == size       # structure: {size: {hash: [list of files]}}
                                                 and (file.type == requested_ext
                                                      or requested_ext == '')]
                                         for hash_ in files_hashes}
                                  for size in files_sizes}

        for size, hashes in files_with_same_hashes.items():
            print(f"\n{size} bytes")
            for hash_, files in hashes.items():
                if len(files) > 1:
                    print('Hash:', hash_)
                    for file in files:
                        print(f"{n}. {file}")
                        file.id = n  # save number of file in output, so we can address by it for deleting
                        n += 1

        break
    elif duplicates == 'no':
        break
    else:
        print("Wrong option")

while True:
    print("Delete files?")
    deleting = input()
    if deleting == 'yes':
        while True:
            print("Enter file numbers to delete:")
            try:
                files_to_delete = [int(n) for n in input().split()]
                if len(files_to_delete) > n - 1 or len(files_to_delete) == 0:  # solve problem with empty and overnumbered inputs
                    print("Wrong format")
                else:
                    freed_space = delete_files(files_to_delete)
                    print(f"Total freed up space: {freed_space} bytes")
                    break
            except ValueError:  # bad desicion but cant think better. Just catch inputs that cant be converted in int()
                print("Wrong format")
        break
    elif deleting == 'no':
        break
    else:
        print("Wrong option")
