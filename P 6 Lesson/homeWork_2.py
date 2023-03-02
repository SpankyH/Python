# 2. Постройте мне следующую картину. (квадратная таблица умножения)

# 1 2 3 4 5 6 7 8 9
# 2 4
# 3 6
# 4 8
# 5 10
# 6 12....

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end=" - ")
    print()


line = [1,2,3,4,5,6,7,8,9]
column = [1,2,3,4,5,6,7,8,9]
for i in line:
    for j in column:
        print(i*j, end=" | ")
    print()