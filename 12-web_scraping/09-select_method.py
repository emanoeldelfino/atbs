import bs4

exampleFile = open('07-example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))  # elems is a list of Tag objects.
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))  # The Tag object as a string.
print(elems[0].getText())
print(elems[0].attrs)

pElems = exampleSoup.select('p')
for elem in pElems:
    print(str(elem))
    print(elem.getText())

# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())
