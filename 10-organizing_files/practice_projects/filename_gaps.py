import os
from pathlib import Path
from natsort import natsorted
import send2trash
import shutil


def remove_gaps(folder, path='.', prefix='spam', extension='py'):
    """
    Find all files with a given prefix in a single
    folder, closing any gaps between numbering.
    """
    extension = '.' + extension if extension and extension[0] != '.' else extension

    path = Path(path)

    files = [filename for filename in os.listdir(
        path / folder) if filename.startswith(prefix) and Path(filename).suffix == extension]
    files = natsorted(files)

    # Get numbers, though it's not necessary.
    # numbers = [int(filename.lstrip(prefix).rstrip(extension)) for filename in files]

    newfilenames = [f'{prefix}{number+1:0>3}{extension}' for number in range(len(files))]

    for oldname, newname in zip(files, newfilenames):
        if oldname != newname:
            shutil.copy(path / folder / oldname, path / folder / newname)
            send2trash.send2trash(path / folder / oldname)  # os.unlink(oldname)


def add_gaps(folder, path='.', prefix='spam', extension='py', index=0):
    """
    Find all files with a given prefix in a single
    folder, adding gaps at index between numbering.
    index is the index of the file to add a gap.
    """
    extension = '.' + extension if extension and extension[0] != '.' else extension

    path = Path(path)

    files = [filename for filename in os.listdir(
        path / folder) if filename.startswith(prefix) and Path(filename).suffix == extension]
    files = natsorted(files)[index:]
    files.reverse()

    # Get numbers, though it's not necessary.
    # numbers = [int(filename.lstrip(prefix).rstrip(extension)) for filename in files]
    num = 2 if index >= 1 else 1
    newfilenames = [
        f'{prefix}{number+num:0>3}{extension}' for number in range(len(files) + 1) if number >= index]
    newfilenames.reverse()

    for oldname, newname in zip(files, newfilenames):
        shutil.copy(path / folder / oldname, path / folder / newname)
        send2trash.send2trash(path / folder / oldname)  # os.unlink(oldname)


remove_gaps(folder='test', prefix='test')
# add_gaps(folder='test', prefix='test')
