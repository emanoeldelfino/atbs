from pathlib import Path
import os


def list_files(path=os.getcwd(), patterns=['*'], size=False, total=False):
    p = Path(path)
    file_names = []
    sizes = []
    full_path = {}
    total_size = 0

    for pattern in patterns:
        for file_path in p.glob(pattern):
            file_name = file_path.name
            full_path[file_name] = file_path
            if file_name not in file_names:
                file_names.append(file_name)

    if size:
        for file_name in file_names:
            size = os.path.getsize(full_path[file_name])
            if total:
                total_size += size
            sizes.append(str(size) + ' bytes')

    value = None
    if file_names:
        value = file_names
        if size:
            value = list(zip(file_names, sizes))
        if total:
            value.append(('/TOTAL/', str(total_size) + ' bytes'))
            # I used '/' in total to differentiate it from file names.
            # '/' can't be used in linux file names, so this is a way to ensure
            # total size of files in bytes don't get confused with other file names.

    return value


path = str(input('Path (empty for current): '))

py_files = list_files(path=path, patterns=['py*', '*.py'], size=True, total=True)

if py_files is not None:
    for file, size in py_files:
        print(file.ljust(20, '.'), size)
else:
    print('No python file found in the given path.')
