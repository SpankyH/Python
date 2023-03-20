# 1. Написать программу с классом One и двумя атрибутами A и B. Написать 4 метода (*+/-). Выполнить эти методы передавая в параметры A и B.

class One:
    a = 0
    b = 0
    def multi(self):
        print(self.a, '*', self.b, '=', self.a * self.b)
    def summ(self):
        print(self.a, '+', self.b, '=',self.a + self.b)
    def dev(self):
        print(self.a, '/', self.b, '=',self.a // self.b)
    def minus(self):
        print(self.a, '-', self.b, '=', self.a - self.b)

same = One()
same.a = 10
same.b = 5

same.multi()
same.summ()
same.dev() 
same.minus() 


