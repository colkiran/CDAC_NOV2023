
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

emp1 = Employee("Mark", 75000)
print(emp1)
print("-" * 60)

print([tch for tch in emp1])


print(len(emp1))
