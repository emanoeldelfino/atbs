#! python3
# findHttps.py - Finds url that begins with http(s) on the clipboard.

import pyperclip
import re

httpRegex = re.compile(r'''(
    (http(s)?://)          # http/https
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    (/%&/*[a-zA-Z])*       # final
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in httpRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No http(s) url were found.')
