
class Animal:
    def __init__(self):
        print('Animal Ctor.......')
        self.a = 10

    def eat(self):
        print("Animals eat......")

    def fun(self):
        print("Greetings Animal.....")

class Person:
    def __init__(self):
        print("Person Ctor......")
        self.p = 20

    def walk(self):
        print("Person walks.......")

    def fun(self):
        print("Greetings Person.....")


# multiple inheritance
class Girl(Animal, Person):
    def __init__(self):
        super().__init__()      # parent class
        Person.__init__(self)
        print("Girl Ctor.....")
        self.g = 30

    def talk(self):
        print("Girls talk.......")

tina = Girl()
tina.walk()
tina.eat()
tina.talk()
print(tina.__dict__)

print("-" * 60)
tina.fun()          # which fun is called?