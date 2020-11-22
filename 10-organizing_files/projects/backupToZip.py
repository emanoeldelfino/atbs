#! python3
# backupToZip.py - Copies an entire folder and its content into
# a ZIP file whose filename increments.

import zipfile
import os
from pathlib import Path


def backupToZip(folder, exts=[], no_exts=[]):
    # Make sure the extensions have a dot at the beggining
    for i, ext in enumerate(exts):
        exts[i] = '.' + ext if ext[0] != '.' else ext
    for i, ext in enumerate(no_exts):
        no_exts[i] = '.' + ext if ext[0] != '.' else ext

    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should used based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # TODO: Create the ZIP file.
    print(f'Creating {zipFilename}...')

    with zipfile.ZipFile(zipFilename, 'w') as backupZip:
        for foldername, subfolders, filenames in os.walk(folder):
            print(f'Adding files in {foldername}...')
            # Add the current folder the ZIP file.
            backupZip.write(foldername)

            # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                if exts and Path(filename).suffix in exts or no_exts and Path(filename).suffix not in no_exts:
                    newBase = os.path.basename(folder) + '_'
                    if filename.startswith(newBase) and filename.endswith('.zip'):
                        print(f'{filename} skipped because it\'s from backup.')
                        continue  # don't back up the backup ZIP files
                    backupZip.write(os.path.join(foldername, filename))
                elif not exts and not no_exts:
                    newBase = os.path.basename(folder) + '_'
                    if filename.startswith(newBase) and filename.endswith('.zip'):
                        print(f'{filename} skipped because it\'s from backup.')
                        continue  # don't back up the backup ZIP files
                    backupZip.write(os.path.join(foldername, filename))

    # TODO: Walk the entire folder tree and compress the files in each folder.
    print('\nDone.')


backupToZip('/home/emanoel/code/automatetheboringstuff', no_exts=['.py', 'txt'])
