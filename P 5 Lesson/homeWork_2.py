# 2. Вывести четные числа из диапазона от 0 до числа который я буду вводить с клавиатуры.

vvod = int(input('Вести число: '))
for i in range(vvod):
    if i % 2 or i == 0:
        continue
    print(i)