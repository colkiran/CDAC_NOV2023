
class Player:
    def __init__(self):     # constructor
        print("Player Initialized......")

    def get_runs(self):
        print('Runs scored.......')

sachin = Player()
sourav = Player()
sachin.__init__()

print("-" * 60)
sachin.get_runs()
sourav.get_runs()
