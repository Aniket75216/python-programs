# Shopping cart with constructor and destructor

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append((name, price, quantity))

    def remove_product(self, name):
        self.products = [
            product for product in self.products
            if product[0] != name
        ]

    def total_bill(self):
        total = 0
        for name, price, quantity in self.products:
            total += price * quantity
        return total

    def display(self):
        print("Customer:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:", self.products)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Amit", "C101")

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 800, 2)

cart.display()

cart.remove_product("Mouse")

print("\nAfter removing Mouse:")
cart.display()

del cart
