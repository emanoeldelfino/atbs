#! python3
# regex_search_arg.py - Search for regex patterns in .txt files in a folder.
# Usage: py.exe regex_search_arg.py folder 'regex_pattern'
# OBS: regex_pattern shouldn't include r'', just type the pattern without any other thing.

import os
import re
import sys

if len(sys.argv) == 3 and '\\' in sys.argv[2]:
    folder = sys.argv[1]
    files = os.listdir(folder)

    regex_pattern = sys.argv[2]
    regex = re.compile(rf'{regex_pattern}')

    count = 1

    for file in files:
        if file[-4:] == '.txt':
            with open(f'{folder}{os.sep}{file}', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    # Searches for any line that maches the user-supplied
                    # regular expression and print it to the screen.
                    mo = regex.search(line)
                    if mo:
                        print()
                        print(f'{count}\n{line}')
                        count += 1
else:
    print('Invalid command. Try py.exe regex_search_arg.py folder <\'regex_pattern\'>')
    print('You can also double the backslashes and it\'ll work.')
