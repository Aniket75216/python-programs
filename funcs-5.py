# 14. Electricity Bill Using Slabs
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    return bill

units = int(input("Enter units consumed: "))
print("Electricity Bill =", electricity_bill(units))


# 15. Gross Salary
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))


# 16. Total Bill with Discount
def total_bill(prices, quantities):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

prices = [1000, 500, 200]
quantities = [2, 3, 4]
print("Final Bill =", total_bill(prices, quantities))
