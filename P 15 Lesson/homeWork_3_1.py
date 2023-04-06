# 3.1. парсит заголовки 2,3 уровня и все span (В СПИСКИ)

import requests
from bs4 import BeautifulSoup


res = requests.get('https://automarine.ru/eng/index.html')
pars = BeautifulSoup(res.text, 'html.parser')

h2s = []
h3s = []
spans = []


for h2 in pars.find_all('h2'):
    h2s.append(h2.text)
print('================ Заголовки H2 ================', *h2s, sep='\n')

for h3 in pars.find_all('h3'):
    h3s.append(h3.text)
print('================ Заголовки H3 ================', *h3s, sep='\n')

for span in pars.find_all('span'):
    spans.append(span.text)
print('================ SPANS ================', *spans, sep='\n')