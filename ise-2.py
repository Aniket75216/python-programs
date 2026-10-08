a=2
for i in range (1,11,1):
    print(a,"x",i,"=",i*a) 
    import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Tablet", "Laptop"],
    "Category": ["Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics", "Electronics"],
    "Quantity": [2, 5, 3, 4, 6, 2, 1],
    "Price": [50000, 20000, 50000, 15000, 20000, 15000, 50000]
}
df = pd.DataFrame(data)

df["Sales"] = df["Quantity"] * df["Price"]

print("Sales Data:")
print(df)

total_sales = np.sum(df["Sales"])
print("\nTotal Sales:", total_sales)

average_sales = np.mean(df["Sales"])
print("Average Sales:", average_sales)

product_sales = df.groupby("Product")["Quantity"].sum()
best_product = product_sales.idxmax()

print("Best Selling Product:", best_product)
print("Quantity Sold:", product_sales.max())

category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)