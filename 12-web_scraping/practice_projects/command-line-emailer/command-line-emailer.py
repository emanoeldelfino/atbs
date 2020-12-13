from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyinputplus as pyip
from time import sleep
import sys

if len(sys.argv) in range(2, 4):
	creds = sys.argv[1]
	with open(creds, 'r') as f:
		content = f.read()

	email, passwd, *_ = content.split('\n')
else:
	email = pyip.inputEmail('\nE-mail: ')
	passwd = pyip.inputPassword('Password: ')

if len(sys.argv) == 3:
	msg = sys.argv[2]
	with open(msg, 'r') as f:
		content = f.read()
	to_email, subject, *body_lines = content.split('\n')
else:
	to_email = pyip.input('\nTo E-mail: ')
	subject = input('Subject: ')

	print('Body (content) (Ctrl + C to finish):')
	while True:
		try:
			body_lines += [input()]
		except KeyboardInterrupt:
			break

browser = webdriver.Firefox()
browser.get('https://login.live.com/')

browser.set_window_position(0, 0)
browser.maximize_window()

login = browser.find_element_by_css_selector("input[type='email']")
login.send_keys(email)
login.send_keys(Keys.ENTER)

sleep(3)

password = browser.find_element_by_css_selector("input[name='passwd'][type='password']")
password.send_keys(passwd)
password.submit()

sleep(5)

browser.get('https://outlook.com')

sleep(3)

buttons = browser.find_elements_by_css_selector("button[type='button'][data-is-focusable='true']")
for i in range(1, 3):
	print(i)
	buttons[i].click()

sleep(10)

to_box = browser.find_element_by_css_selector("input[aria-label='To']")
to_box.send_keys(to_email)

subject_box = browser.find_element_by_css_selector("input[aria-label='Add a subject']")
subject_box.send_keys(subject)

body_box = browser.find_element_by_css_selector("div[dir='ltr'][role='textbox']")

for body_line in body_lines:
	body_box.send_keys(body_line)
	body_box.send_keys(Keys.ENTER)

body_box.send_keys(Keys.CONTROL, Keys.ENTER)

