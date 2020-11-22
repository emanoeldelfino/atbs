#! python3
# clean_arg.py - Clean empty files and directories.

# Usage: py.exe clean_arg.py    [directories] - Delete empty files and directories in directory.
#        py.exe clean_arg.py -f [directories] - Delete only empty files in directory.
#        py.exe clean_arg.py -d [directories] - Delete only empty directories in directory.

# Notes: If directories aren't specified the current one is set as default.

import os
import sys
from pathlib import Path
import pyinputplus as pyip

args = sys.argv[1:]

if len(args) == 1 and args[0] == '--help':
    print('Usage: ')
    print('py.exe clean_arg.py    [dirs] - Delete empty files and directories in dirs.')
    print('py.exe clean_arg.py -f [dirs] - Delete only empty files in dirs.')
    print('py.exe clean_arg.py -d [dirs] - Delete only empty directories in dirs.')
    print('If dirs is not defined, the current working directory is set by default.')
    sys.exit()

arg = args[:1] if args and args[0] in ['-f', '-d'] else []

# Directories that will be cleaned, default is current directory.
directories = [directory for directory in args[len(arg):]] if args[len(arg):] else ['.']
valid_directories = all(Path(directory).is_dir() for directory in directories)

if valid_directories:
    empty_folders = []
    empty_files = []

    for path in directories:
        for folder, subfolders, files in os.walk(path):
            if not arg or arg == ['-d']:
                if not os.listdir(folder):
                    empty_folders.append(folder)

            if not arg or arg == ['-f']:
                for file in files:
                    # if os.stat(folder + os.sep + file).st_size == 0:
                    c_file = Path(folder) / file
                    if os.stat(c_file).st_size == 0:
                        empty_files.append(c_file)

    for folder in empty_folders:
        print(folder)

    for file in empty_files:
        print(file)

    if empty_folders:
        print('\n{} empty folders were found.'.format(len(empty_folders)))

    if empty_files:
        print('\n{} empty files were found.'.format(len(empty_files)))

    if empty_files or empty_folders:
        confirm = pyip.inputYesNo(prompt='\nAre you sure you want to delete these stuff? [y/n] ')
        if confirm == 'yes':
            for folder in empty_folders:
                os.rmdir(folder)
            for file in empty_files:
                os.remove(file)
    else:
        print('Nothing was found.')
else:
    print('Invalid operation.')
    print('For help type py.exe clean_arg.py --help')
