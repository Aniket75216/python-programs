# 22. Hospital Bill
def consultation_charge():
    return 500

def laboratory_charge():
    return 1000

def medicine_charge():
    return 1500

def room_charge(days):
    return days * 1000

def final_bill(days, category):
    total = (consultation_charge() +
             laboratory_charge() +
             medicine_charge() +
             room_charge(days))

    if category == "senior":
        discount = total * 0.20
    elif category == "child":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount

days = int(input("Enter room days: "))
category = input("Enter category: ")
print("Final Hospital Bill =", final_bill(days, category))


# 23. Shopping Cart / Invoice
def subtotal(products):
    total = 0
    for name, price, quantity in products:
        total += price * quantity
    return total

def coupon_discount(total):
    if total >= 5000:
        return total * 0.20
    elif total >= 2000:
        return total * 0.10
    else:
        return 0

def gst(amount):
    return amount * 0.18

def invoice(products):
    sub = subtotal(products)
    discount = coupon_discount(sub)
    amount = sub - discount
    tax = gst(amount)
    final = amount + tax

    print("Subtotal =", sub)
    print("Discount =", discount)
    print("GST =", tax)
    print("Final Amount =", final)

products = [
    ("Laptop", 50000, 1),
    ("Mouse", 1000, 2),
    ("Keyboard", 2000, 1)
]
invoice(products)


