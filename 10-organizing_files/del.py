import os
import pyinputplus as pyip
from pathlib import Path
from files import list_files
import shutil

folders = input('\nSelected folders [separate with spaces]: ').split()
file_ext = input('File type that will be deleted [empty for entire folder(s)]: ')

if file_ext and file_ext[0] != '.':
    file_ext = '.' + file_ext

try:
    folders = [Path(folder) for folder in folders]
    is_folder = [folder.is_dir() for folder in folders]
    assert all(is_folder)
except AssertionError:
    print('\nInvalid folder.')
else:
    files = []
    if file_ext:
        for folder in folders:
            for filename in folder.glob('*' + file_ext):
                files.append(filename)
                print(filename)
    else:
        for folder in folders:

            list_files(str(folder))

    if files or folders:
        confirm = pyip.inputYesNo(prompt='Are you sure you want to delete these stuff? ')

        if confirm == 'yes':
            if file_ext:
                for folder in folders:
                    for filename in folder.glob('*' + file_ext):
                        os.unlink(filename)
            else:
                for folder in folders:
                    shutil.rmtree(folder)
    else:
        print('\nNo files/folders found.')
