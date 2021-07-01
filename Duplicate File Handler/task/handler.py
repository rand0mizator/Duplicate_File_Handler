import sys
import os


class File:
    def __init__(self, name_of, path_to, size_of, type_of):
        self.name = name_of
        self.path = path_to
        self.size = size_of
        self.type = type_of

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

try:
    root_path = sys.argv[1]  # reading command line argument [0] - its script file itself, [1] - its path to root folder
    if os.path.isdir(root_path) or os.path.isfile(root_path):
        for root, dirs, files in os.walk(root_path):
            for name in files:
                path_to_file = os.path.join(root, name)
                object_size = os.path.getsize(path_to_file)
                object_head, object_type = os.path.splitext(path_to_file)
                all_files.append(File(name, path_to_file, object_size, object_type))  # creating list of objects
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

for size in files_sizes:
    print(f"\n{size} bytes")
    for file in all_files:
        if file.type == requested_ext or requested_ext == '':
            if file.size == size:
                print(file)
