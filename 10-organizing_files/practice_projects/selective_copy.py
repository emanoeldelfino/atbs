import os
import shutil
from pathlib import Path


def copy_from(folder, path='.', exts=['pdf', '.jpg'], new_folder='copied_files'):
    """
    -> walk through a folder tree searching by files with
    certain file extensions (such as .pdf or .jpg)
    """
    path = Path(path)
    list_of_files = []
    for i, ext in enumerate(exts):
        exts[i] = '.' + ext if ext[0] != '.' else ext

    for current, subs, files in os.walk(path / folder):
        for file in files:
            if Path(file).suffix in exts:
                list_of_files.append(file)

    # Copy these files from whatever location they are in to a new folder.
    os.mkdir(new_folder)
    for file in list_of_files:
        shutil.copy(file, path / new_folder / file)

    print(f'The files were successfully copied to the new folder.')


copy_from('.', exts=['md'], new_folder='my_files2')
