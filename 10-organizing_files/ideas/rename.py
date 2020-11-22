#! python3
# renameDates.py - Renames filenames adding a spefic prefix

import shutil
import os
import pyinputplus as pyip
from pathlib import Path


def add_prefix_to(path, prefix='', numbered=False):
    path = Path(path)
    if prefix:
        print()
        files = os.listdir(path)
        for filename in files:
            print(f'{filename} -> {prefix}_{filename}')
        confirm = pyip.inputYesNo('\nAre you sure you want to rename these files? ')
        if confirm == 'yes':
            for filename in files:
                shutil.move((path / filename).resolve(), path / f'{prefix}_{filename}')

    if numbered:
        print()
        files = os.listdir(path)
        for i, filename in enumerate(files, 1):
            print(f'{filename} -> {i}_{filename}')
        confirm = pyip.inputYesNo('\nAre you sure you want to rename these files? ')
        if confirm == 'yes':
            for i, filename in enumerate(files, 1):
                shutil.move((path / filename).resolve(), path / f'{i}_{filename}')


def add_index_to(path, start=1):
    path = Path(path)
    files = os.listdir(path)
    print()
    for i, filename in enumerate(files, start):
        print(f'{filename} -> {i}_{filename}')
    confirm = pyip.inputYesNo('\nAre you sure you want to rename these files? ')
    if confirm == 'yes':
        for i, filename in enumerate(files, start):
            shutil.move((path / filename).resolve(), path / f'{i}_{filename}')


add_prefix_to('test', prefix='prefix', numbered=True)
# add_index_to('test', start=-100)
