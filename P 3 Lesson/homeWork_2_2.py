# 2. есть ли 18 лет
# есть 18 лет = входи
# нет = запрет
while True:
    age = str(input('Вам есть 18 лет?: '))
    if age == 'Да' or age == 'да' or age == 'Yes' or age == 'yes' or age == 'y':
        print('Добро пожаловать!')
    else:
        print('Доступ запрещён!!!')