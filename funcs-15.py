# 45. Employees - filter, map and sorted
employees = [
    ("Aniket", "IT", 60000),
    ("Rahul", "HR", 45000),
    ("Amit", "IT", 70000),
    ("Rohit", "Sales", 55000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

increased = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)

sorted_employees = sorted(employees, key=lambda x: x[2])

print("Above 50000:", high_salary)
print("After 10% increase:", increased)
print("Sorted:", sorted_employees)


# 46. Products - Total Value, Filter and Sort
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 10000, 1)
]

values = list(
    map(lambda x: (x[0], x[1], x[2], x[1] * x[2]), products)
)

filtered = list(
    filter(lambda x: x[1] > 1000, products)
)

sorted_products = sorted(values, key=lambda x: x[3])

print("Total values:", values)
print("Price > 1000:", filtered)
print("Sorted:", sorted_products)


# 47. Words - map, filter and sorted
words = ["apple", "banana", "cat", "elephant", "dog", "computer"]

lengths = list(map(lambda x: len(x), words))
long_words = list(filter(lambda x: len(x) > 5, words))
sorted_words = sorted(words, key=lambda x: len(x))

print("Lengths:", lengths)
print("More than 5 characters:", long_words)
print("Sorted:", sorted_words)
