# 1. парсит страницу целиком и выводит всю информацию в консоль;

import requests
from bs4 import BeautifulSoup

res = requests.get('https://automarine.ru/eng/index.html')
print(res.text)