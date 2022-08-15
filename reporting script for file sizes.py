import os
from os.path import abspath, join, getsize

parent = input('Enter file path to parent directory: ')
print(parent)

sizes = {}

option = input('select option: 1) show files larger than 500 kilobytes; 2) show files larger than 1 megabytes ')

for top_dir, directories, files in os.walk(parent):
    for _file in files:
        
        full_path = abspath(join(top_dir, _file))
        file_size = getsize(full_path)
        
        if option == '1' and file_size/1000 > 500:
            sizes[full_path] = getsize(full_path)
        elif option == '2' and file_size/1000000 > 1:
            sizes[full_path] = getsize(full_path)

sorted_results = sorted(sizes, key=sizes.get, reverse=True)     

for path in sorted_results[:10]:
    print("Path: {0}, size: {1}".format(path, sizes[path]/1000000))