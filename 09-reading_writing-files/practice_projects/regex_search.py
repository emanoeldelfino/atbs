import os
import re

folder = input('\nFolder: ')
files = os.listdir(folder)

user_regex = input('\nRegular Expression: \n > ')
regex = re.compile(rf'{user_regex}')

# Read all .txt files from folder.
for file in files:
    if file[-4:] == '.txt':
        with open(f'{folder}{os.sep}{file}', 'r') as f:
            lines = f.readlines()
            for line in lines:
                # Searches for any line that maches the user-supplied
                # regular expression and print it to the screen.
                mo = regex.search(line)
                if mo:
                    print(line, end='\n\n')
