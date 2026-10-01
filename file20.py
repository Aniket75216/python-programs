# Calculate deposits, withdrawals and final balance

filename = "transactions.txt"

transactions = [
    "deposit,10000",
    "withdraw,2000",
    "deposit,5000",
    "withdraw,1500"
]

with open(filename, "w") as file:
    for transaction in transactions:
        file.write(transaction + "\n")

total_deposits = 0
total_withdrawals = 0
largest = 0

with open(filename, "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")
        amount = float(amount)

        largest = max(largest, amount)

        if transaction == "deposit":
            total_deposits += amount
        elif transaction == "withdraw":
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest)\n