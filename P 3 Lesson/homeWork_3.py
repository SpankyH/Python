# 3. Пользователь вводит два целых числа. Выведите меньшее из них. 

while True:
    num1 = int(input('Первое число: '))
    num2 = int(input('Второе число: '))
    text = 'Меньшее число:'
    if num1 < num2:
        print('{} {}'.format(text,num1))
    elif num2 < num1:
        print('{} {}'.format(text,num2))
    else:
        print('Числа равны')