# ATM menu-driven program

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_details(self):
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(10001, "Amit", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display_details()
    elif choice == 5:
        print("Thank you for using ATM.")
        break
    else:
        print("Invalid choice.")
