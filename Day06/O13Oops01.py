

class Player:                   # pascal casing

    def get_runs(self):
        print("Runs Scored......")


sachin = Player()           # calls the default constructor
print(type(sachin))
sachin.get_runs()
print(sachin.__class__)     # double underscore - dunder-class

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
