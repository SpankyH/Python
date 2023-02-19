# 3. Хочу еще посчитать сумму всех чисел, что делятся на 3 от 0 до числа который я буду вводить с клавиатуры 

vvod = int(input('Вести число: '))
vyvod = 0
for i in range(vvod):
    if i % 3:
        continue
    else:
         vyvod += i
    # print(vyvod, end=" ")
print(vyvod)