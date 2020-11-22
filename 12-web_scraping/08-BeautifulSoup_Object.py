import requests
import bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text)
# print(noStarchSoup)  # html of the page
print(type(noStarchSoup))


exampleFile = open('07-example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile)
# print(exampleSoup)  # html of the page
print(type(exampleSoup))
