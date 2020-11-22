#! python3
# mercadolivredup.py - Save all products links.

import requests
import sys
import os
import bs4
from pathlib import Path

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

# https://informatica.mercadolivre.com.br/portateis-e-acessorios-notebook/gamer

args = sys.argv[1:]
if len(args) != 1:
    print('Invalid command. \nTry: py.exe mercadolivredup.py <url>')
    sys.exit()

url = args[0]

# os.makedirs(Path(url).parts[1], exist_ok=True)

main_folder = url.replace('https://', '').replace('/', '∕')
os.makedirs(main_folder, exist_ok=True)

page = 1

while True:
    # foldername = url.replace('https://', '').replace('/', '∕')
    # os.makedirs(Path(foldername), exist_ok=True)

    # os.makedirs(main_folder / page, )

    logging.debug('url: %s ' % url,)
    res = requests.get(url, headers={'User-Agent': 'Custom'})
    res.raise_for_status()

    # filename = Path(url)

    # with open(Path(main_folder).joinpath(filename)), 'wb') as urlFile:
    with open(Path(main_folder) / (str(page).zfill(2) + '.html'), 'wb') as urlFile:
        for chunk in res.iter_content(100000):
            urlFile.write(chunk)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    next_url = soup.select('ul li.andes-pagination__button--next a.andes-pagination__link')

    if not next_url:
        break

    url = next_url[0].get('href')

    page += 1
