
from collections import namedtuple

nmdTpl = namedtuple("Students", "studid studname age cls")

stud = nmdTpl(studid= 101, studname="Jack", age=12, cls='7th std')
print(stud)
print("-" * 60)

print(f"Student ID   :{stud.studid}")
print(f"Student Name :{stud.studname}")
print(f"Age          :{stud.age}")
print(f"Class        :{stud.cls}")

# stud.studname = "Mike"
