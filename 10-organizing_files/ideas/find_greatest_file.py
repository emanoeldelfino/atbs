#! python3
# find_greatest_file.py - Find greatest file in numbers and in
# current working directory

import os
from pathlib import Path


def find_greatest_files(path):
    greatest_size = [0, '']
    greatest_numf = [0, '']
    folders = [Path(folder) for folder in os.listdir(path) if Path(folder).is_dir()]
    for folder in folders:
        # oneliner
        folder_size = sum(f.stat().st_size for f in folder.glob('**/*') if f.is_file())
        for current, subs, files in os.walk(folder):
            if folder_size > greatest_size[0]:
                greatest_size[0] = folder_size
                greatest_size[1] = current
            if len(os.listdir(current)) > greatest_numf[0]:
                greatest_numf[0] = len(os.listdir(current))
                greatest_numf[1] = current

    return greatest_size, greatest_numf


big = find_greatest_files('.')
print(big)
