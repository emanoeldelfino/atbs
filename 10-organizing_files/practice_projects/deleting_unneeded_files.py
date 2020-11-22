import os
from pathlib import Path


def get_large(folder, path='.', size=20):
    """
    walk through a folder tree and search by
    exceptionally large files or folders.

    :size: Size in MB.
    """
    path = Path(path)
    large = []

    for current, dirs, files in os.walk(path / folder):
        # Get folder size, as size is given in bytes we
        # divide it by  1 million to get the size in MB.
        folder_size = round(sum(f.stat().st_size for f in Path(
            current).glob('**/*') if f.is_file()) / 1000000, 2)
        if folder_size > size:
            large.append((Path(current).resolve(), folder_size))
        for file in files:
            file_size = round(os.path.getsize(Path(current) / file) / 1000000, 2)
            if file_size > size:
                large.append(((Path(current) / file).resolve(), file_size))

    return large


large_stuff = get_large('.')

for stuff, size in large_stuff:
    print(f'{size} MB -> {stuff}')
