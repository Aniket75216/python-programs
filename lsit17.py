cart = ["Milk", "Bread", "Butter"]

cart.append("Sugar")
cart.remove("Bread")

item = "Milk"

if item in cart:
    print("Item Found")

print("Cart:", cart)
print("Total Items:", len(cart))