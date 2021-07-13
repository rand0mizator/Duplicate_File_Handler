import sys
import os
import hashlib


class File:
    def __init__(self, name_of, path_to, size_of, type_of, hash_of):
        self.name = name_of
        self.path = path_to
        self.size = size_of
        self.type = type_of[1:]
        self.hash = hash_of

    def __str__(self):
        return f"{self.path}"


def sorter(list_of_objects, order):
    """Sorting passed list of files or folders by its size"""
    if order == '1':  # descending
        return sorted(list_of_objects, key=lambda x: -x.size)
    elif order == '2':  # ascending
        return sorted(list_of_objects, key=lambda x: x.size)


all_files = []
files_sizes = []
files_hashes = []
same_size = {size: file for size in files_sizes for file in all_files if file.size == size}

try:
    root_path = 'D:\\Перенос\\Документы'  #sys.argv[1]  # reading command line argument [0] - its script file itself, [1] - its path to root folder
    if os.path.isdir(root_path) or os.path.isfile(root_path):
        for root, dirs, files in os.walk(root_path):
            for name in files:
                hash_of_file = hashlib.md5()
                path_to_file = os.path.join(root, name)
                object_size = os.path.getsize(path_to_file)
                object_head, object_type = os.path.splitext(path_to_file)
                with open(path_to_file, 'rb') as f:
                    hash_of_file.update(f.read())
                all_files.append(File(name, path_to_file, object_size, object_type, hash_of_file.hexdigest()))  # creating list of objects
                                                                                      # Class File
except IndexError:
    print("Directory is not specified")

requested_ext = input("Enter file format:").strip()
option = None

while True:
    print("""Size sorting options:\n1. Descending\n2. Ascending""")
    option = input("Enter a sorting option:\n")
    if option in ['1', '2']:
        break
    else:
        print("Wrong option")


all_files = sorter(all_files, option)  # sort files in provided order

for file in all_files:  # creating list of different sizes of objects
    if file.size not in files_sizes:
        files_sizes.append(file.size)
    if file.hash not in files_hashes:
        files_hashes.append(file.hash)

same_size = {size: [file for file in all_files if file.size == size]for size in files_sizes}
for size, files in same_size.items():
    print(size)
    for file in files:
        print(file)
same_hash = {size: {hash_: [file for file in all_files if file.size == size and file.hash == hash_]
                    for hash_ in files_hashes}
             for size in files_sizes}
for size, hashes in same_hash.items():
    print(size)
    for hash_, files in hashes.items():
        #print(hash_)
        for file in files:
            print(file, hash_)

# for size in files_sizes:
#     print(f"\n{size} bytes")
#     for file in all_files:
#         if file.type == requested_ext or requested_ext == '':
#             if file.size == size:
#                 print(file)

# while True:
#     print("""\nCheck for duplicates? yes\\no""")
#     duplicates = input(">")
#     if duplicates in ['yes', 'no']:
#         break
#     else:
#         print("Wrong option")

# if duplicates == 'yes':
#     n = 1
#     for size in files_sizes:
#         print(f"\n{size} bytes")
#         for hash_ in files_hashes:
#             print(f"Hash: {hash_}")
#             for file in all_files:
#                 if file.hash == hash_:
#                     print(f"{n}. {file}")
#                     n += 1


