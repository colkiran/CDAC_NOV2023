
class Animal:

    def __init__(self):
        print("Animal Ctor.......")
        self.age = 1

    def eat(self):
        print("Animals eat.......")


class Bird(Animal):
    def fly(self):
        print("Birds fly.......")


class Fish(Animal):

    def fish(self):
        print("fishes swim....")

