
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account Ctor.....")

    @abstractmethod
    def getBalance(self):
        pass

    def withdraw(self):
        pass

class Savings(Account):

    def getBalance(self):
        print("The balance in the account ending XXXX8934 is 85000.00")

    def deposit(self):
        print('Amount successfully credited into the account.........')

sav = Savings()
sav.deposit()
sav.getBalance()