from pathlib import Path
from files import list_files
import send2trash

folders = input('\nFolders to be deleted [separate with spaces]: ').split()
file_ext = input('File type that will be deleted [empty for entire folder]: ')

try:
    folders = [Path(folder) for folder in folders]
    is_folder = [folder.is_dir() for folder in folders]
    assert all(is_folder)
except AssertionError:
    print('Invalid folder.')
else:
    if file_ext:
        if file_ext[0] != '.':
            file_ext = '.' + file_ext
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
