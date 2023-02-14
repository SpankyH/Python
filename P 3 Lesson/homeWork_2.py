# 2. есть ли 18 лет
# есть 18 лет = входи
# нет = запрет
while True:
    birthYear = int(input('Ваш год рождения?: '))
    if birthYear <= 2006:
        print('Добро пожаловать!')
    else:
        print('Доступ запрещён!')

