
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary            #instance variables

    # it works on not Equal to also
    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Kenith", 45000)
emp2 = Employee("Kevin", 41000)

print(str(emp1))
print(emp1)             # implicitly call __str__

print("-" * 60)
# == comparison
# by default it compares the address
if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

if (emp1 < emp2):
    print("{}'s salary of {} is greater than {}'s salary {}".format(emp2.name, emp2.salary, emp1.name, emp1.salary))
else:
    print("{}'s salary of {} is greater than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

print(emp1 >= emp2)