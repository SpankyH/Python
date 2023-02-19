############ ЦИКЛЫ ############ FOR
# Итерация - Одно повторение цикла

# range(stop) -  (ДО значения)
# range(start,stop) -  (ОТ и ДО значения)
# range(start,stop,step) - (ОТ и ДО значения с ШАГОМ)
# start - первый элемент последов.
# stop - последний элемент последов.
# step - шаг.





############ ПРИМЕРЫ ############

# for i in range(1,10):  # Элемент в Диапазоне()
#     print(i)
####
# stop (ДО значения)
# for i in range(13):
#   print(i)
####
# start-stop (ОТ и ДО значения)
# for i in range(13,15):
#     print(i)
####
# start-stop-step (ОТ и ДО значения с ШАГОМ)
# for i in range(13,100,13):
#     print(i)
####
# for i in range(1,13):
#     if i == 7:
#         continue
#     print(i)
####
# for i in range(1,13):
#     if i == 7:
#         break
#     print(i)
####
# list = ['AAAA','BBBB','CCCC','DDDD']
# for i in list:
#     print(i)
####
# a = "STALKER"
# for i in a:
#     print(i, end=".")
##################### вывести STALKER как S.T.A.LK.ER ###############