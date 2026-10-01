# banking package

from banking.account import create_account, balance
from banking.transaction import deposit, withdraw
from banking.loan import loan_amount

account = create_account("Amit", 10000)

print("Account:", account)
print("Balance:", balance(account))

deposit(account, 5000)
withdraw(account, 2000)

print("Final Balance:", balance(account))
print("Loan Amount:", loan_amount(100000, 10, 2))\n