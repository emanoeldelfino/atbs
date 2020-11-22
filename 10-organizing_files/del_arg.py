#! python3
# del_arg.py - Delete files inside folders.
# Usage:
# py.exe del_arg.py <folder1> [folder2] - Delete entire folders with its files.
# py.exe del_arg.py <folder1> [folder2] -e <ext1> [ext2] - Delete files with the extension in folder.

import os
import sys
import shutil
import pyinputplus as pyip
from pathlib import Path
from files import get_files, list_files_2

args = sys.argv[1:]

if args:
    if '-e' in args:
        folders = args[:args.index('-e')]
        exts = args[args.index('-e') + 1:]
        if not exts or not folders:
            print('Invalid command.')
            sys.exit()
    else:
        folders = args
        exts = []

    for i, ext in enumerate(exts):
        if ext[0] != '.':
            exts[i] = '.' + ext


else:
    print('Invalid command.')

try:
    folders = [Path(folder) for folder in folders]
    is_folder = [folder.is_dir() for folder in folders]
    assert all(is_folder)
except AssertionError:
    print('Invalid folder.')
else:
    files_list = get_files('.', folders=folders, exts=exts)

    list_files_2('.', folders=folders, exts=exts)

    confirm = pyip.inputYesNo(prompt='\nAre you sure you want to delete these stuff? ')

    if confirm == 'yes':
        if exts:
            for file in files_list:
                os.unlink(file)
        else:
            for folder in folders:
                shutil.rmtree(folder)
