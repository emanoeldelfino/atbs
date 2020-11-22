from pathlib import Path
import os
import sys
import shutil
import pyinputplus as pyip
import send2trash
import zipfile


def choice(options: list, start: int = 1) -> int:
    for i, option in enumerate(options, start):
        print(f'{i}. {option}')

    while True:
        try:
            opt = int(input('\nOption: '))
        except (ValueError, TypeError):
            print('\nInvalid value. Try again.')
        except KeyboardInterrupt:
            print()
            sys.exit()
        else:
            if opt not in range(start, len(options) + start):
                print('\nError, invalid option. Try again.')
            else:
                break
    return opt


def rm_dups(lists: list) -> list:
    no_dups_lists = []
    for listx in lists:
        no_dups_lists.append(list(set(listx)))
    return no_dups_lists


def copy(files: list, folder: str = 'copied_files') -> None:
    if not Path(folder).is_dir():
        os.mkdir(folder)
    for file in files:
        shutil.copy(file, Path('.') / folder)


def delete(files: list) -> None:
    for file in files:
        os.unlink(file)


def safe_delete(files: list) -> None:
    for file in files:
        send2trash.send2trash(file)


def compress(files: list, path: str = 'compressed_files') -> None:
    path = Path(str(folder_name) + '.zip') if str(path)[-4:] != '.zip' else path

    with zipfile.ZipFile(path.name, 'w') as new_zip:
        for file in files:
            new_zip.write(file, compress_type=zipfile.ZIP_DEFLATED)


def move(files: list, folder: str = 'moved_files') -> None:
    if not Path(folder).is_dir():
        os.mkdir(folder)
    for file in files:
        shutil.move(str(file), str(Path('.') / folder))


def add_index(files: list) -> None:
    for i, file in enumerate(files):
        f = Path(file)
        shutil.move(file, f.parents[0] / Path(f'{i}{f.name}'))


print('\nYou can separate multiple inputs with spaces.')
print('Leave empty for getting the exclude option.')
print('If both include and exclude are empty it\'ll get everything by default')

# Inside current path
folders = input('\nFolders: ').split()
if not folders:
    no_folders = input('\nExcluded folders: ').split()
    current = os.listdir('.')
    folders = [folder for folder in current if folder not in no_folders] if no_folders else current

# Inside folders and subfolders of subfolders
subfolders = input('\nSubfolders: ').split()
no_subfolders = []
if not subfolders:
    no_subfolders = input('\nExcluded subfolders: ').split()

filetypes = input('\nFile types: ').split()
no_filetypes = []
if not filetypes:
    no_filetypes = input('\nExcluded file types: ').split()

for types in [filetypes, no_filetypes]:
    for i, filetype in enumerate(types):
        types[i] = '.' + filetype if filetype[0] != '.' else filetype

lists = folders, subfolders, no_subfolders, filetypes, no_filetypes
folders, subfolders, no_subfolders, filetypes, no_filetypes = rm_dups(lists)

list_of_files = []

print()

for folder in folders:
    if subfolders:
        for root, dirs, files in os.walk(folder):
            level = root.replace(folder, '').count(os.sep)
            indent = ' ' * 4 * (level)
            subindent = ' ' * 4 * (level + 1)

            directory_name = Path(root).name
            print(f'{indent}{directory_name}')
            if directory_name in subfolders:
                for file in files:
                    if filetypes and Path(file).suffix in filetypes:
                        print(f'{subindent}{file}')
                        list_of_files.append(Path(root) / file)
                    elif no_filetypes and Path(file).suffix not in no_filetypes:
                        print(f'{subindent}{file}')
                        list_of_files.append(Path(root) / file)
                    elif not filetypes and not no_filetypes:
                        print(f'{subindent}{file}')
                        list_of_files.append(Path(root) / file)
    elif no_subfolders:
        for root, dirs, files in os.walk(folder):
            dirs[:] = [directory for directory in dirs if directory not in no_subfolders]
            level = root.replace(folder, '').count(os.sep)
            indent = ' ' * 4 * (level)
            subindent = ' ' * 4 * (level + 1)

            directory_name = Path(root).name
            print(f'{indent}{directory_name}')
            for file in files:
                if filetypes and Path(file).suffix in filetypes:
                    print(f'{subindent}{file}')
                    list_of_files.append(Path(root) / file)
                elif no_filetypes and Path(file).suffix not in no_filetypes:
                    print(f'{subindent}{file}')
                    list_of_files.append(Path(root) / file)
                elif not filetypes and not no_filetypes:
                    print(f'{subindent}{file}')
                    list_of_files.append(Path(root) / file)
    else:
        for root, dirs, files in os.walk(folder):
            level = root.replace(folder, '').count(os.sep)
            indent = ' ' * 4 * (level)
            subindent = ' ' * 4 * (level + 1)

            directory_name = Path(root).name
            print(f'{indent}{directory_name}')

            for file in files:
                if filetypes and Path(file).suffix in filetypes:
                    print(f'{subindent}{file}')
                    list_of_files.append(Path(root) / file)
                elif no_filetypes and Path(file).suffix not in no_filetypes:
                    print(f'{subindent}{file}')
                    list_of_files.append(Path(root) / file)
                elif not filetypes and not no_filetypes:
                    print(f'{subindent}{file}')
                    list_of_files.append(Path(root) / file)

if list_of_files:
    print()
    print('=' * 30)
    option = choice(['Copy files',
                     'Delete files (irreversible)',
                     'Safe delete files',
                     'Compresss files',
                     'Move files',
                     'Add index (rename)'])

    if option in [1, 4, 5]:
        folder_name = input('\nName of the folder where files will be stored: ')

    if option == 1:
        copy(list_of_files, folder_name)
    elif option == 2:
        confirm = pyip.inputYesNo(
            prompt='\nAre you sure you want to permanently delete these files? ')
        if confirm == 'yes':
            delete(list_of_files)
    elif option == 3:
        safe_delete(list_of_files)
    elif option == 4:
        compress(list_of_files, folder_name)
    elif option == 5:
        move(list_of_files, folder_name)
    elif option == 6:
        add_index(list_of_files)
else:
    print('No files found.')
