# QUESTION 5
# Create a dictionary containing Order_ID, Customer, Product,
# Quantity, Price and Discount.
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount
# Then display:
# 1. All orders
# 2. Orders above 5,000
# 3. Highest-value order
# 4. Average order value
# ============================================================

orders = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [1, 2, 1, 2, 3],
    "Price": [60000, 25000, 30000, 15000, 8000],
    "Discount": [2000, 1000, 1500, 500, 300]
}

df = pd.DataFrame(orders)

print("\nQUESTION 5")

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("\nAll Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:")
print(df["Final_Amount"].mean())


# ============================================================
