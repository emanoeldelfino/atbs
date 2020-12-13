#! /usr/bin/env python3
# img_site_downloader.py - Search for photos in flickr and download it.

import sys
from selenium import webdriver
from time import sleep
import os
import requests

if len(sys.argv) == 2:
	search = sys.argv[1]

	directory = 'downloaded-' + search + '-images'
	os.makedirs(directory, exist_ok=True)

	driver = webdriver.Firefox()

	driver.set_window_position(0, 0)
	driver.maximize_window()

	driver.get(f'https://www.flickr.com/search/?text={search}')
	
	sleep(15)

	img_elems = driver.find_elements_by_css_selector('div.photo-list-photo-view')
	img_styles = [img_elem.get_attribute('style') for img_elem in img_elems]
	properties = [props for props in [img_style.split(';') for img_style in img_styles]]
	bg_properties = [prop for props in properties for prop in props if prop.strip().startswith('background-image')]
	urls = ['https:' + prop[24:-2] for prop in bg_properties]

	for i, url in enumerate(urls, 1):
		num = str(i).zfill(3)
		r = requests.get(url)	
		with open(f'{directory}/{num}' , 'wb') as img:
			for chunk in r.iter_content(chunk_size=1024*1024):
				if chunk:	
					img.write(chunk)
		print('Downloaded %s/%s from %s' % (directory, num, url))

	driver.quit()
else:
	print('Invalid command.')
	print(f'Try: python {__file__} <search>')

