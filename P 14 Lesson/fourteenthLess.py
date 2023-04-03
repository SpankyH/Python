############ ООП ############



############ Примеры ############

# class Animal:
#     def eat(self):
#         print("Give me a food, please.")

#     def sleep(self):
#         print("Don't touch me! I sleep!!!")


# class Cat(Animal):
#     def destroy(self):
#         print("I broke something.")

# cat1 = Cat()
# cat1.eat()
# cat1.sleep()
# cat1.destroy()

####

# class Car():
#     def __init__(self):
#         self.__maxprice = 1500

#     def sell(self):
#         print(format(self.__maxprice))
#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Car()
# c.sell()

# c.__maxprice = 1000
# c.sell()

# c.setMaxPrice(1000)
# c.sell()

####

# class Movie():
#     def render(self):
#         print("render")

# class Film(Movie):
#     def render(self):
#         print("render film")

# class Anime(Movie):
#     def render(self):
#         print("render anime")

# f1 = Film()
# f1.render()

# a1 = Anime()
# a1.render()

####

# class Human():
#     def __init__(self, name):
#         self.name = name
#     def answer(self, question):
#         print("ВОПРОС: ")

#     def __str__(self):
#         return f'{self.name}'
    
# class Erik(Human):
#     def ask(self, someone, question):
#         print(f'{someone}, {question}')
#         someone.answer(question)
#         print()

# super
        