############ Объектно Ориентированное Программирование ############

# Объект - сущность имеющая атрибуты и поведение
# Имя КЛАССА всегда с большой буквы !!!!!!!!!!
# def calc(self)  - SELF - ССЫЛКА НА ИЗМЕНЕНИЕ ТЕКУЩЕГО ЭКЗЕМПЛЯРА КЛАССА


############ ПРИМЕРЫ ############
# class Cat:
#     age =0
#     name = ""
# Cat1 = Cat()
# Cat1.name = 'Miay'
# Cat1.age = 30
# Cat2 = Cat()
# Cat2.name = 'Murr'
# Cat2.age = 22
# print(f"{Cat1.name} is {Cat1.age} Years old")
# print(f"{Cat2.name} is {Cat2.age} Years old")
####
# class Evg:
#     age = 0
#     money = 0
#     def calc(self):
#         print('Evg =',self.age * self.money)
# Evg1 = Evg()
# Evg1.age = 35
# Evg1.money = 1000
# Evg1.calc()
####
# class Wtf:
#     def __init__(self, name =""):
#         self.name = name
#         print(name)
# Wtf1 = Wtf("What the... ?")