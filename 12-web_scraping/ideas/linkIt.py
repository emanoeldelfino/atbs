#! /usr/bin/env python3
# ~/bin
# linkIt.py - Open all links if only one page is given, otherwise
# it'll open all the pages given.
import webbrowser
import sys
import pyperclip
import requests
import re

page = ''
if len(sys.argv) == 2:
    page = sys.argv[1]
elif len(sys.argv) == 1:
    page = pyperclip.paste()
else:
    links = [link for link in sys.argv[1:]]

if page:
    page = 'http://' + page if page[:8] != 'http://' else page
    try:
        res = requests.get(page)
        res.raise_for_status()
        html = res.text
    except Exception as err:
        print('An error has occurred: %s' % (err))
    else:
        link_regex = re.compile(
            r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))')
        page_links = link_regex.findall(html)
        links = [link[0] for link in page_links]

for link in links:
    try:
        webbrowser.open(link)
    except Exception as err:
        print('An error has occurred: %s' % (err))
    else:
        print('Successfully opened %s.' % (link))

# Version 2.0

# linkIt2.py - Save clipboard to a text file(links.txt) and then
# opens all browsers from this file.

# import webbrowser
# import pyperclip

# links = pyperclip.paste().split()
# with open('links.txt', 'w') as f:
#     for link in links:
#         f.write(link + '\n')

# with open('links.txt', 'r') as f:
#     lines = f.readlines()

# for line in lines:
#     try:
#         webbrowser.open(line)
#     except Exception as err:
#         print('An error has occurred %s' % (err))
