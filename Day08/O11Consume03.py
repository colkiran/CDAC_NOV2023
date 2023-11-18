
import sys

sys.path.append("C:\\Delhi")
print(sys.path)

# gugaon - package
import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Satish")

ply1 = Player("Satish", 23)
ply1.get_details()
