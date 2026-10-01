# QUESTION 7
# A retail shop maintains sales information in a Python
# dictionary containing Product_ID, Product_Name, Category,
# Price and Quantity.
# Write a Python program to:
# 1. Convert dictionary into Pandas DataFrame.
# 2. Add a new column Total_Sales.
# 3. Calculate total sales using Price × Quantity.
# 4. Display products with sales greater than 10,000.
# 5. Find product with maximum sales.
# 6. Calculate average sales.
# ============================================================

retail = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 20000, 1200, 15000, 10000],
    "Quantity": [2, 3, 10, 2, 4]
}

df = pd.DataFrame(retail)

print("\nQUESTION 7")

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\nDataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage sales:")
print(df["Total_Sales"].mean())


# ============================================================


# QUESTION 7 - PANDAS SERIES
# Create a Pandas Series using a dictionary where student
# names are keys and marks are values.
# Perform:
# 1. Display the Series.
# 2. Display marks of a particular student.
# 3. Find maximum and minimum marks.
# 4. Calculate average marks.
# 5. Display students who scored more than 75.
# ============================================================

student_marks = {
    "Amit": 80,
    "Rahul": 72,
    "Sneha": 90,
    "Priya": 68,
    "Rohit": 85
}

series = pd.Series(student_marks)

print("\nQUESTION 7 - PANDAS SERIES")
print(series)

print("\nMarks of Sneha:")
print(series["Sneha"])

print("\nMaximum Marks:")
print(series.max())

print("\nMinimum Marks:")
print(series.min())

print("\nAverage Marks:")
print(series.mean())

print("\nStudents scoring more than 75:")
print(series[series > 75])


# ============================================================
