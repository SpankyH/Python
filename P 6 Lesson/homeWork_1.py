# 1. Напишите программу, которая будет в лесенку выстраивать числа ДО произвольного положительного числа .
# То есть если я введу цифру 5 то у меня получится
# 1
# 12
# 123
# 1234
# 12345
                

num = int(input("Ввести число: "))
for i in range(1,num+1):
        for j in range(1, i+1):
            print(j, end='')
        print()
