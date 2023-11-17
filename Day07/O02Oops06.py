
class Player:

    def  __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fname, lname, age):       # factory
        print("Factory....")
        # calls the constructor
        return cls(f"{fname} {lname}", age)


ply1 = Player("Dhoni", 32)
ply1.get_details()
print("-" * 60)

ply2 = Player.createPlayer("Virat", "Kholi", 28)
ply2.get_details()
