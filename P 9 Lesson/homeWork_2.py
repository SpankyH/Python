# 2. Напишите функцию, которая будет выводить информацию о всех файлах и подкаталогах в произвольной папке на вашем пк

import os

def info(path):
    print(os.listdir(path))

info('G:\\STEAMGAMES\steamapps\common')