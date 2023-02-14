# 2. Вывести на экран все четные значения от 1 до 100


start = 0
while start <= 100:
    start += 1
    if start % 2:
        continue
    print(start, end=" ")