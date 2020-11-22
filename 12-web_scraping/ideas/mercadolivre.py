#! python3
# searchpypi.py - Opens several search results.

import requests
import sys
import webbrowser
import bs4

opn = False
args = sys.argv[1:]

# pegar opiniões do produto
if args[0] == '-o':
    args = sys.argv[2:]
    opn = True

print('Pesquisando...')

res = requests.get('https://lista.mercadolivre.com.br/' + ' '.join(args))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.ui-search-result__content')

numOpen = min(5, len(linkElems))

if not opn:
    for i in range(numOpen):
        urlToOpen = linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)
else:
    for i in range(numOpen):
        urlToOpen = linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)

        # Opinion/Review part
        resOpn = requests.get(urlToOpen)
        resOpn.raise_for_status()

        soupOpn = bs4.BeautifulSoup(resOpn.text, 'html.parser')
        opnElem = soupOpn.select('.ui-pdp-reviews__comments__button')[0]
        opnUrl = 'https://mercadolivre.com.br' + opnElem.get('href')
        print('Opening Opionions', opnUrl)
        webbrowser.open(opnUrl)
