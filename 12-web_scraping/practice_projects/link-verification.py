#! /usr/bin/env python

import requests
import bs4
import sys
from pathlib import Path
import os

folder = Path('files')
os.makedirs(folder)

args = sys.argv[1:]

if not args or len(args) > 1:
	print('Invalid command.')
	print(f'Try: python {__file__} <url>') 
	sys.exit()

try:
	link = args[0] if args[0].startswith('https://') else 'https://' + args[0]
	res = requests.get(link)
	res.raise_for_status()
except Exception as err:
	print(err)
else:
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	links = [link.get('href') for link in soup.find_all('a') if link.get('href').startswith('https://')]
	
	for i, link in enumerate(links, 1):
		res = requests.get(link)
		if res.status_code == 404:
			print(f'Broken link {link}')
		else:
			with open(Path(folder / (str(i).zfill(2) + '.html')), 'wb') as lnk:
				for chunk in res.iter_content(chunk_size=100000):
					lnk.write(chunk)
			print(f'Download {link} in {folder}/{i:02d}.html')

