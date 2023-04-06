# 3. парсит заголовки 2 и 3 уровня и все span со страницы.

import requests
from bs4 import BeautifulSoup

res = requests.get('https://automarine.ru/eng/index.html')
pars = BeautifulSoup(res.text, 'html.parser')

for h2 in pars.find_all('h2'):
    print(h2.text)

for h3 in pars.find_all('h3'):
    print(h3.text)

for span in pars.find_all('span'):
    print(span.text)