import bs4

soup = bs4.BeautifulSoup(open('07-example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') is None)
print(spanElem.attrs)
