#! python3
# del_secure_arg.py - Delete files inside folders.
# Usage:
# py.exe del_secure_arg.py -f folder1 folder2 - Delete entire folders with its files.
# py.exe del_secure_arg.py -e folder1 folder2 <file_extension> - Delete files with the extension in
# folder.

from pathlib import Path
from files import list_files
import send2trash
import sys

if len(sys.argv) >= 3 and sys.argv[1] in ['-f', '-e']:
    if sys.argv[1] == '-f':
        folders = list(sys.argv)[2:]
        file_ext = ''
    else:
        folders = list(sys.argv[2:-1])
        file_ext = sys.argv[-1]

        if file_ext[0] != '.':
            file_ext = '.' + file_ext

    try:
        folders = [Path(folder) for folder in folders]
        is_folder = [folder.is_dir() for folder in folders]
        assert all(is_folder)
    except AssertionError:
        print('Invalid folder.')
    else:
        if file_ext:
            for folder in folders:
                for filename in folder.glob('*' + file_ext):
                    print(filename)
        else:
            for folder in folders:
                list_files(str(folder))

        if file_ext:
            for folder in folders:
                for filename in folder.glob('*' + file_ext):
                    send2trash.send2trash(filename)
        else:
            for folder in folders:
                send2trash.send2trash(folder)

        print('\nMoved to trash.')
else:
    print('Invalid operation.')
