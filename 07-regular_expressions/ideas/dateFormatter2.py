#! python3

import pyperclip
import re


def repl(match):

    # format: mm/dd/yyyy
    if match.group(1) != None:
        month, day, year = match.group(2), match.group(4), match.group(6)

    # format: yyyy/mm/dd
    elif match.group(7) != None:
        year, month, day = match.group(8), match.group(10), match.group(12)

    if day[0] == '0':
        day = day[1]

    if month[0] == '0':
        month = month[1]

    return day + '/' + month + '/' + year  # format: dd/mm/yyyy


dateRegex = re.compile(r'''(
         ([1][0-2]|0\d|\d)           # month
         (/|-)                       # sep
         (3[01]|[12]\d|0\d|\d)       # day
         (/|-)                       # sep
         (\d{4})                     # year
         )
     |
                           (
         (\d{4})                     # year
         (/|-)                       # sep
         ([1][0-2]|0\d|\d)           # month
         (/|-)                       # sep
         (3[01]|[12]\d|0\d|\d)       # day
         )''', re.VERBOSE)

text = str(pyperclip.paste())
new = dateRegex.sub(repl, text)

pyperclip.copy(new)
print('Copied to clipboard')
print(new)
