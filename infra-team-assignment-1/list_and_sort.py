# -*- coding: utf-8 -*-
import os
import heapq

directory = input("Enter directory ")
num_files = int(input("Enter no of files to list "))

file_names = (os.path.join(path, name) for path, _, filenames in os.walk(directory)
              for name in filenames)

file_sizes = ((name, os.path.getsize(name)) for name in file_names)
big_files = heapq.nlargest(num_files, file_names, key=os.path.getsize)

for b in big_files:
    print("{}MB\t{:>}".format(os.path.getsize(b) >> 20, b))

input("Now sorting files")

# get the desktop path
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
list_of_files_and_folders = os.listdir(desktop)
list_of_files = []
for fname in list_of_files_and_folders:
    f_path = os.path.join(desktop, fname)
    if os.path.isfile(f_path) and not (os.path.islink(f_path) or f_path[-3:] == 'lnk'):
        list_of_files.append(f_path)

extensions = dict()
for fname in list_of_files:
    if '.' in fname:
        extension = fname.split('.')[-1:][0]  # get the extension as a string not as a list
        if extension in extensions:
            extensions[extension].append(fname)
        else:
            extensions[extension] = [fname]
    else:
        if 'no_extension' in extensions:
            extensions['no_extension'].append(fname)
        else:
            extensions['no_extension'] = [fname]

documents = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')
for extension, file_list in extensions.iteritems():
    target_dir = os.path.join(documents, extension)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # just to avoid importing shutil when we already have os
    for fpath in file_list:
        fname = os.path.basename(fpath)
        os.rename(fpath, os.path.join(target_dir, fname))
input("Done")
