#! python3
# guj.py - Downloads recent forum threads from braziliam programming web forum GUJ

from pathlib import Path
import requests
import os
import bs4
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

url = 'https://www.guj.com.br/latest'
foldername = url.replace('https://', '').replace('/', '∕')

os.makedirs(foldername, exist_ok=True)  # store messages in folder

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
links = [link.get('href') for link in soup.select('.raw-topic-link')]
logging.debug('soup %s' % (soup.select('.latest-topic-list-item')))

# Download links.

for link in links:
    print('Downloading link %s' % (link))

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
