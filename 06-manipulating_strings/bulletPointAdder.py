#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import sys
import pyperclip

if len(sys.argv) > 1:
    print('Usage: python bulletPointAdder.py')
    sys.exit()

text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
new_lines = ['* ' + line for line in lines]
# for i in range(len(lines)):    # loop through all indexes in the "lines" list
#    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

new_text = '\n'.join(new_lines)

pyperclip.copy(new_text)

print('Succesfuly executed!')
