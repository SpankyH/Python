# 1. Найти сумму чисел от 1 до 100 результат в консоль конечно же


start = 1 # начальное число
target = 0 # целевое число
while start <= 100: # пока начальное <= 100
    # print(target, end=" ")
    target += start # прибавлем начальное к целевому
    start += 1 # каждый цикл начальное увеличиваем на 1
print(target)