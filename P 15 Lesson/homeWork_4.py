############### 4  КАРТИНКИ С САЙТА ##############
import os
import bs4
import requests
from bs4 import BeautifulSoup
# from pathlib import Path
# path = Path(__file__)


res = requests.get("https://automarine.ru/eng/index.html")
pictures = BeautifulSoup(res.content,'html.parser')

for img in pictures.find_all(class_="img-fluid"):
    link = img['src']
    link = link.replace('..','https://automarine.ru')
    with open("EXAMPLE.png".format(link),"wb") as f:
        f.write(requests.get(link).content)
        link = link.replace('https://automarine.ru/img/', "")
        f.close()
        # print(link)
        os.rename('EXAMPLE.PNG', link)
        # if link in path:
        #     continue
        
