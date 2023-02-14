# 3. Вывести на экран все не четные значения от 1 до 300


start = 0
while start < 300:
    start += 1
    if start % 2:
        print(start, end=" ")