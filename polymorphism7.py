# Bank interest polymorphism

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


for account in [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]:
    print("Interest:", account.calculate_interest(50000))\n