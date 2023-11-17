
class Employee:

    def __init__(self, name):
        self.__name = name      # Private Variable
        self.tech = ['C', 'C++', 'JAVA', 'Spring', 'Hibernate', 'Angular JS']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])


emp1 = Employee("Rahul")
print(emp1)
# emp1.name = "Rahul Dravid"      # add new key value in __dict__
print(emp1.__dict__)
emp1._Employee__name = "Rahul Dravid"
print(emp1)
print(emp1.__dict__)