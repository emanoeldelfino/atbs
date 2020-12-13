from selenium import webdriver
import pyinputplus as pyip
import sys

repository_name = ''
if len(sys.argv) in range(2, 4):
	login = sys.argv[1]
else:
	login = input('\nUsername or Email: ')

if len(sys.argv) == 3:
	repository_name = sys.argv[2]	
else:
	repository_name = input('Repository to create (empty for not creating): ')

password = pyip.inputPassword('\nPassword: ')

browser = webdriver.Chrome()
browser.get('https://github.com')

browser.set_window_position(2000, 0)
browser.maximize_window()

browser.find_element_by_link_text('Sign in').click()

login_elem = browser.find_element_by_id('login_field')
password_elem = browser.find_element_by_id('password')

login_elem.send_keys(login)
password_elem.send_keys(password)

login_elem.submit() 

print('\nLogged to GitHub.')

if repository_name:
	browser.find_element_by_link_text('New').click()

	repo_name = browser.find_element_by_id('repository_name')

	repo_name.send_keys(repository_name)

	private_button = browser.find_element_by_id('repository_visibility_private')
	private_button.click()

	private_button.submit()

	print(f'\nCreated {repository_name} private repository.')

