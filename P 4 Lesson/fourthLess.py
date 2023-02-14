############ ЦИКЛЫ ############
# while - Универсальный
# for - Поэлементный
#(переменная,  end=" ") - запись в одной строке
#### ОПЕРАТОРЫ ####
# break - прерывание
# continue - запуск заново



############ ПРИМЕРЫ ############
# a = 1
# while a <= 10:
#     print(a)
#     a += 1
####
# a = False
# b = 6
# c = 18
# d = 12
# while not a and b <= d <= c:
#     if c == d:
#         print('Done')
#     else:
#         print(c - d)
#     d += 1
####
# a = 30
# b = 40
# while a < b:
#     print(a)
#     a += 3
####
# a = 'Пример'
# while a:
#     print(a, end=" ")
#     a = a[:-1]
####
# a = 0
# while True:
#     if a == 10:
#         break
#     print(a)
#     a += 1
####
# a = 10
# while a:
#     a -= 1
#     if a % 2 != 0:
#         continue
#     print(a)