import os
import send2trash
from pathlib import Path

# list files from startpath which are inside folders and have exts.


def list_files(startpath: object, exclude: list = []):
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [directory for directory in dirs if directory not in exclude]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        subindent = ' ' * 4 * (level + 1)

        print(f'{indent}{os.path.basename(root)}')
        for file in files:
            print(f'{subindent}{file}')


def get_files(path: object, folders: list, exts: list = []) -> list:
    listf = []
    path = Path(path)
    for folder in folders:
        if exts:
            for ext in exts:
                ext = '.' + ext if ext[0] != '.' else ext
                listf += folder.glob(f'**/*{ext}')
        else:
            listf += folder.glob(f'**/*')  #
    return listf


def list_files_2(path: object, folders: list, exts: list = []):
    """
    List files in path inside folders by exts.

    :path: the path where folders will be.
    :folders: the list of folders to list the files.
    :exts: optional. The extension of files that will be searched.
    """
    path = Path(path)
    listf = []

    if not folders:
        folders = os.listdir(path)

    startpaths = [path.resolve() / folder for folder in folders]
    valid_startpaths = all(startpath.is_dir() for startpath in startpaths)

    if startpaths and valid_startpaths:
        for startpath in startpaths:
            for root, dirs, files in os.walk(startpath):
                level = root.replace(str(startpath), '').count(os.sep)
                indent = ' ' * 4 * (level)
                subindent = ' ' * 4 * (level + 1)

                print(f'{indent}{os.path.basename(root)}/')

                if exts:
                    for ext in exts:
                        ext = '.' + ext if ext[0] != '.' else ext
                        listf += [file for file in Path(root).glob('*' + ext)]

                    if listf:
                        for file in listf:
                            print(f'{subindent}{file.name}')
                else:
                    listf += [Path(root) / file for file in files]

                    for file in listf:
                        print(f'{subindent}{file.name}')

    else:
        return None


def safe_delete_file(path=os.getcwd(), ext=''):
    for folder, subfolders, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                path = os.path.join(folder, file)
                print('Deleted: ', path)
                send2trash.send2trash(path)
