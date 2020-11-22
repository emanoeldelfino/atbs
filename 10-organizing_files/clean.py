import os
from pathlib import Path
import pyinputplus as pyip

path = Path(input('Give an absolute or relative path to clean empty directories\n > '))
# if path.is_dir():
#     os.listdir(path))
empty_folders = []
for folder, subfolders, files in os.walk(path):
    if not os.listdir(folder):
        empty_folders.append(folder)

for folder in empty_folders:
    print(folder)

if empty_folders:
    print('{} empty folders were found.'.format(len(empty_folders)))
    confirm = pyip.inputYesNo(prompt='Do you want to delete them? [y/n] ')
    if confirm == 'yes':
        for folder in empty_folders:
            os.rmdir(folder)
else:
    print('No empty folders were found.')
