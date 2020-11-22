#! python3
# backup_entire_site.py - Downloads HTML from a site and its links.
# python backup_entire_site.py <url>

from pathlib import Path
import requests
import os
import bs4
import sys
import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

args = sys.argv[1:]

if len(args) != 1:
    print('Invalid command.')
    print('Try: python backup_entire_site.py <url>')
else:
    url = args[0]  # starting url
    foldername = url.replace('https://', '').replace('/', '∕')
    os.makedirs(foldername, exist_ok=True)  # store pages in folder

    # Download the page
    print('Downloading page %s...' % url)

    res = requests.get(url)
    res.raise_for_status()

    with open(Path(foldername).joinpath(foldername), 'wb') as urlFile:
        for chunk in res.iter_content(100000):
            urlFile.write(chunk)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the links of page
    # links = [link.get('href') for link in soup.select('a')]
    links = soup.findAll('a', attrs={'href': re.compile('^https://')})

    # Download links.
    for link in links:
        # print('Downloading link %s...' % (link))
        link = link.get('href')

        try:
            res = requests.get(link)
            res.raise_for_status()

            filename = Path(link).name

            # Save link HTML to folder.
            linkFile = open(os.path.join(foldername, filename), 'wb')
            for chunk in res.iter_content(100000):
                linkFile.write(chunk)
            linkFile.close()
        except Exception as err:
            print('Error Downloading %s' % (link))
            print('Error: %s' % (err))
        else:
            print('Download complete for %s' % link,)

    print('Done.')
