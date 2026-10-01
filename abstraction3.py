# Abstract bank account

from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class CurrentAccount(SavingsAccount):
    pass


account = SavingsAccount()
account.deposit(10000)
account.withdraw(3000)

print("Balance:", account.balance)\n