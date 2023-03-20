# 2. Написать програмуу с классом Студент, с тремя атрибутами(Имя, Номер, Возраст). Создать 5 методов: 1 - Получение данных об имени; 2 - Получение данных об возрасте; 3 - Получение данных о номере; 4 - Измененние данных возраста; 5 - Измененние данных группы

class Student:
    name = ""
    num = 0
    age = 0
    group = ""
    def name1(self):
        print('Имя: ', self.name)
    def age1(self):
        print('Возраст: ', self.age)
    def num1(self):
        print('Номер тел.: ', self.num)
    def chage(self, age=''):
        self.age = age
        print('Новый возраст: ', age)
    def chgroup(self, group=''):
        self.group = group
        print('Группа: ', group)


student1 = Student()
student1.group = 'Абитуриент'
student1.name = 'Евгений'
student1.num = '+7(999)123-45-67'
student1.age = 34

student1.chgroup('Студент')
student1.name1()
student1.age1()
student1.num1()

student1.chage(40)
