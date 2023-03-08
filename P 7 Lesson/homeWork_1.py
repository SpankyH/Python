# 1. Напишите функцию которая будет сумировать все целые числа от первого до второго параметра, если первый параметр будет больше второго, то поменяйте их местами.


# def summ(first,second):
#     if first > second:
#         second = first
#         first = second
#     for i in range(int(input("Первое: ")),int(input("Второе: "))):
#         first += 1
#         print(i)
# print(summ)


def summ(num1,num2):
    znachenie = 1
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range(num1,num2):
        znachenie += i
    return znachenie
    
print(summ(int(input("Первое: ")),int(input("Второе: "))))

