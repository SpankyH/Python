# 1. Напишите функцию, которая будет открывать заранее созданый тхт файл и выводить содержимое на экран (тхт создать самим и наполнить)

def openfile(file):
    with open(file) as document:
        read_file = document.read()
    print(read_file)

openfile('nine.txt')