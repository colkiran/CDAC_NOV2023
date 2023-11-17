
class Employee:

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary  # instance variables
        self.tech = ['C', 'C++', 'JAVA', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


    def append(self, val):
        self.tech.append(val)


emp1 = Employee("Ben", 85000)
print(emp1)
print("-" * 60)

print([tech for tech in emp1])

print("-" * 60)

emp1.append("Python")
print([tech for tech in emp1])

print("-" * 60)

tch = emp1[2]
print(f"tch :{tch}")

print("-" * 60)
 
emp1[4] = "Oracle"

print([tch for tch in emp1])

# x = (1, 2, 3, 4, 5)
# print(f"x :{x}")
# x[3] = 400
