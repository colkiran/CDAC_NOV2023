
class Animal:
    def eat(self):
        print("Animals eat......")

class Bird(Animal):
    def fly(self):
        print('Birds fly.....')

class Chicken(Bird):
    def breed(self):
        print("Chickens are breeded for comsumption" )

    def fly(self):
        print("Chickens seldom fly......")

chic = Chicken()
chic.breed()
chic.fly()          # - parent class
chic.eat()          # - ansistor class

