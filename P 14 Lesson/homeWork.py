# Разработать класс Общение, у которого есть атрибуты к общению.
# Составить 2 допкласса для человека и инопланетянина.
# Они наследуют методы и атрибуты первого класса с добавлением своих функций в зависимости от их различий.


class Comm():
    def talk(self):
        print("I want talk with you")

    def hugs(self):
        print("I need hugs")

class Human(Comm):
    def lie(self):
        print("I'm tolerance to all")
    def badWords(self):
        print("F$%k you a%^#o$@e")

class Alien(Comm):
    def scream(self):
        print("AAAAAAAAAAAAA!!!")

human1 = Human()
alien1= Alien()

human1.talk()
human1.hugs()
human1.lie()
human1.badWords()

alien1.talk()
alien1.hugs()
alien1.scream()

#######


class Communic():
    def talk(self):
        print("I can talk")

class Human(Communic):
    def talk(self):
        print("I'm talking now")

class Alien(Communic):
    def talk(self):
        print("#$%$ ^@#!$!%! @#!%!")

hum1 = Human()
ufo1 = Alien()

hum1.talk()
ufo1.talk()