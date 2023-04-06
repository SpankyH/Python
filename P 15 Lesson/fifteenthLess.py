############ API  ПАРСЕР ############

import requests
from bs4 import BeautifulSoup

# res = requests.get('https://google.com')
# # print(res.text)

# sup = BeautifulSoup(res.text, 'html.parser')
# print(sup.title)

# titles = sup.findAll('h1')
# for title in titles:
#     print(title.text)

# titles = sup.select('h1', class="main-header")
# for title in titles:
#     print(title.text)

######

# res = requests.get('https://flowerline.shop/')
# soup = BeautifulSoup(res.text, 'html.parser')
# for i in soup.descendants:
#     if i.name:
#         print(i.name)
# # print(soup.h1.text)
# # print(soup.find('div', id="page"))
# for tag in soup.find_all('h2'):
#     print(tag.text)
