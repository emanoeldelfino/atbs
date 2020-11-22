#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil
import os
import re

# Create a regex that matches files with the American date format.
zeroPattern = re.compile(r"""^(.*?)  # all text before leading zeros
    (0)+                             # leading zeros
    ([1-9])+                         # numbers
    (.*?)$                           # all text after leading zeros
    """, re.VERBOSE)

files = os.listdir('.')

# Loop over the files in the working directory.
for leading_zero in files:
    mo = zeroPattern.search(leading_zero)

    # Skip files without leading zeros.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    zeroPart = mo.group(2)
    numberPart = mo.group(3)
    afterPart = mo.group(4)

    # Form the no leading zero filename.
    no_leading_zero = beforePart + numberPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    leading_zero = os.path.join(absWorkingDir, leading_zero)
    no_leading_zero = os.path.join(absWorkingDir, no_leading_zero)

    # Rename the files.
    # print(f'Renaming "{leading_zero}" to "{no_leading_zero}"')
    shutil.move(leading_zero, no_leading_zero)  # uncomment after testing
