#! python3
# imgur.py - Open imgur images.
# py.exe imgur.py <search>

import requests
import sys
import webbrowser
import bs4

args = sys.argv[1:]

save = False

search = ' '.join(args)

if not search:
    print('Invalid command.')
    print('Try: py.exe imgur.py <search>')
else:
    print('Searching Images...')

    url = f'https://imgur.com/search?q={search}'

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    linkElems = ['https://imgur.com' + link.get('href')
                 for link in soup.select('.image-list-link')[:10]]

    for link in linkElems:
        print('Opening', link)
        webbrowser.open(link)
