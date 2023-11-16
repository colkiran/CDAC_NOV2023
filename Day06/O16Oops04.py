
class Player():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initiazed......")

    def get_details(self):
        print(f"name is {self.name}\tage is {self.age}")

ply1 = Player("Sachin", 54)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 35)
ply2.get_details()

print("-" * 60)
print("ply1:", ply1.__dict__)
print("ply2:", ply2.__dict__)

print("-" * 60)
ply2.runs = 85
print("ply1:", ply1.__dict__)
print("ply2:", ply2.__dict__)
