#! python3

import pyperclip
import re

dateRegex = re.compile(r'''(
         (1[0-2]|0[1-9]|[1-9])        # month
         (/|-)                        # sep
         (3[01]|[12]\d|0[1-9]|[1-9])  # day
         (/|-)                        # sep
         (\d{4})                      # year
         )
     |
                           (
         (\d{4})                      # year
         (/|-)                        # sep
         ([1][0-2]|0[1-9]|[1-9])      # month
         (/|-)                        # sep
         (3[01]|[12]\d|0[1-9]|[1-9])  # day
         )''', re.VERBOSE)

text = str(pyperclip.paste())

dates = []

for date in dateRegex.findall(text):

    # format: mm/dd/yyyy
    if date[0] != '':
        month, day, year = date[1], date[3], date[5]

    # format: yyyy/mm/dd
    elif date[6] != '':
        year, month, day = date[7], date[9], date[11]

    if day[0] == '0':
        day = day[1]

    if month[0] == '0':
        month = month[1]

    dates.append(month + '/' + day + '/' + year)

if len(dates) > 0:
    pyperclip.copy('\n'.join(dates))
    print('Copied to clipboard')
    print('\n'.join(dates))
else:
    print('No dates found.')
