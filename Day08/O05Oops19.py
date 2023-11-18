
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):
    def doJob(self):
        print("Manager's job.......")

class Developer(Employee):
    def doJob(self):
        print("Developer's Job.........")

def BankFun(emp):
    print("Bank Job Started".center(60, "-"))
    emp.doJob()
    print("Bank Job Ended".center(60,"-"))
    print("-" * 60)
    
mark = Manager()
tina = Developer()

BankFun(mark)
BankFun(tina)