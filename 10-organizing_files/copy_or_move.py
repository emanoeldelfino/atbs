#! python3
# copy_move.py - Copy files inside folder.
# Usage:

# py.exe copy.py [-m] <folder1> [folder2] - Copy entire folder with its files.
# py.exe copy.py [-m] <folder1> [folder2] -e <ext1> [ext2] - Copy files with the extension in folder.
# py.exe copy.py [-m] <folder1> [folder2] [-n] <folder_name> - The name of the folder to copy the files to.

# -c is copy mode which is the default, if you want you can use -m which is move mode.

from pathlib import Path
import os
import sys
import shutil
from files import get_files, list_files_2

mode = sys.argv[1] if sys.argv[1] == '-m' else '-c'

args = sys.argv[2:] if sys.argv[1] == '-m' else sys.argv[1:]

folder_to_save = 'your_files'

if args:
    if '-e' in args and args[-2] != '-n':
        folders = args[:args.index('-e')]
        exts = args[args.index('-e') + 1:]
        if not exts or not folders:
            print('Invalid command.')
            sys.exit()
    elif len(args) >= 2:
        if '-e' in args and '-n' == args[-2]:
            folders = args[:args.index('-e')]
            exts = args[args.index('-e') + 1:-2]
            folder_to_save = args[-1]
        elif '-e' not in args and '-n' == args[-2]:
            folders = args[:-2]
            exts = []
            folder_to_save = args[-1]
        else:
            folders = args
            exts = []
    elif len(args) == 1:
        if args[0] == '--help':
            string = ("py.exe copy.py [-m] <folder1> [folder2] - Copy entire folder with its files\n"
                      "py.exe copy.py [-m] <folder1> [folder2] -e <ext1> [ext2] - Copy files with the "
                      "extension in folder\n"
                      "py.exe copy.py [-m] <folder1> [folder2] [-n] <folder_name> - The name of the "
                      "folder to copy the files to\n"
                      "-c is copy mode which is the default, if you want you can use -m which is move mode")
            print(string)
            sys.exit()
        else:
            folders = args
            exts = []

    for i, ext in enumerate(exts):
        if ext[0] != '.':
            exts[i] = '.' + ext

    try:
        folders = [Path(folder) for folder in folders]
        is_folder = [folder.is_dir() for folder in folders]
        assert all(is_folder)
    except AssertionError:
        print('Invalid folder. Folder doesn\'t exist.')
    else:
        if not Path(folder_to_save).is_dir():
            os.mkdir(folder_to_save)

        files_list = get_files('.', folders=folders, exts=exts)

        list_files_2('.', folders=folders, exts=exts)

        if exts:
            if mode == '-c':
                for file in files_list:
                    shutil.copy(str(file), Path('.') / folder_to_save / file.name)
            elif mode == '-m':
                for file in files_list:
                    shutil.move(str(file), Path('.') / folder_to_save / file.name)
        else:
            if mode == '-c':
                for folder in folders:
                    shutil.copytree(str(folder), Path('.') / folder_to_save / Path(folder).name)
            elif mode == '-m':
                for folder in folders:
                    shutil.move(str(folder), Path('.') / folder_to_save / Path(folder).name)

        word = 'copied' if mode == '-c' else 'moved'
        print(f'\nFiles successfully {word} to {folder_to_save}.')
else:
    print('Invalid command.')
