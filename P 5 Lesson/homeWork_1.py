# 1. Через цикл for хочу посчитать сумму всех числех, которые я буду вводить самостоятельно , скажем от 13 до числа что я введу сам.

vvod = int(input('Вести число: '))
vyvod = 0
for i in range(13,vvod):   
    vyvod += i
    # print(vyvod, end=" ")
print('{}{}'.format('Сумма от 13 до введеного числа = ',vyvod))

vvod = int(input('Вести число: '))
vyvod = 0
for i in range(13,vvod+1):
        vyvod += i
        # print(vyvod, end=" ")
print('{}{}'.format('Сумма от 13 до введеного числа, включительно = ',vyvod))