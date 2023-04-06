# 2. парсит все теги с id about_us через цикл for;


import requests
from bs4 import BeautifulSoup

res = requests.get('https://automarine.ru/eng/index.html')
ids = BeautifulSoup(res.text, 'html.parser')

for tags in ids.find_all('div', id="about_us"):
    print(tags.text)