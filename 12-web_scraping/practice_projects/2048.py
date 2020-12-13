#! /usr/bin/env python
# 2048.py - Plays 2048 game on web.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def send_keys_delay(elem, keys: list, delay=1):
	for key in keys:
		sleep(delay)
		elem.send_keys(key)


options = webdriver.ChromeOptions()

# prefs = {
#     "download.open_pdf_in_system_reader": False,
#     "download.prompt_for_download": True,
#     "plugins.always_open_pdf_externally": False
# }

prefs = {"download_restrictions": 3}

options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(options=options)

browser.set_window_position(0, 0)

browser.maximize_window()

browser.get('https://gabrielecirulli.github.io/2048/')

body = browser.find_element_by_tag_name('body')

keys=[Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

for _ in range(100):
	send_keys_delay(body, keys=keys, delay=2) 	

