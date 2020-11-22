#! python3
# imgur.py - Save imgur images.
# py.exe imgur.py <search>

import requests
import sys
import bs4
import os
from pathlib import Path

args = sys.argv[1:]

search = ' '.join(args)

os.makedirs(search.replace(' ', '_'), exist_ok=True)

if not search:
    print('Invalid command.')
    print('Try: py.exe imgur.py <search>')
else:
    print('\nSearching Images...\n')

    url = f'https://imgur.com/search?q={search}'

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    imgLinks = ['https://' + link.get('src')[2:]
                for link in soup.select('.image-list-link img')[:10]]

    for imgLink in imgLinks:
        res = requests.get(imgLink)
        res.raise_for_status()

        with open(Path(search) / imgLink.replace('/', '∕'), 'wb') as imgFile:
            print(f'Saving: {imgLink}')
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)

        # imageFile = open(Path(search) / imgLink.replace('/', '∕'), 'wb')
        # for chunk in res.iter_content(100000):
        #     imageFile.write(chunk)
        # imageFile.close()
