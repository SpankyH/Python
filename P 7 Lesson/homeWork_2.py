# 2. Напишите функцию, которая будет принимать на себя 2 параметра в виде имени и фамилии студента, а выводить на экран будет запись вида Привет Имя Фамилия.


def welcome(name,surname):
    text1 = 'Привет, ' + name + surname
    return text1
print(welcome('Евгений ','Мартынов'))

def welcome(name,surname):
    text1 = 'Привет, ' + name + " " + surname + '!'
    return text1
print(welcome(str(input("Имя: ")),str(input("Фамилия: "))))
