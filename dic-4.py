# Q26. Create employee salaries dictionary and find highest, lowest, average and employees above ₹50,000.
employees = {"Rahul": 45000, "Amit": 65000, "Sneha": 55000, "Priya": 40000}
print("Highest:", max(employees.values()))
print("Lowest:", min(employees.values()))
print("Average:", sum(employees.values()) / len(employees))
print("Above 50000:", {k: v for k, v in employees.items() if v > 50000})

# Q27. Create product quantities dictionary and perform add, update, delete, search and below-10 operations.
products = {"Pen": 20, "Book": 8, "Bag": 15}
products["Pencil"] = 5
products["Book"] = 10
products.pop("Bag")
print(products)
print("Below 10:", {k: v for k, v in products.items() if v < 10})

# Q28. Create contacts dictionary and implement add, search, update, delete and display.
contacts = {"Rahul": "9876543210", "Amit": "9123456780"}
contacts["Sneha"] = "9999999999"
print("Search:", contacts.get("Amit"))
contacts["Amit"] = "8888888888"
contacts.pop("Rahul")
print(contacts)

# Q29. Create books dictionary and implement add, search, remove, display and count.
books = {101: "Python Programming", 102: "Data Structures"}
books[103] = "Computer Networks"
print("Search:", books.get(101))
books.pop(102)
print("Books:", books)
print("Total:", len(books))

# Q30. Group students according to their department.
students = {"Rahul": "CS", "Amit": "Mechanical", "Sneha": "CS", "Priya": "Electronics"}
groups = {}
for name, department in students.items():
    groups.setdefault(department, []).append(name)
print(groups)

# Q31. Create a dictionary where key is word length and value is list of words having that length.
words = ["cat", "dog", "apple", "bat", "orange", "pen"]
result = {}
for word in words:
    result.setdefault(len(word), []).append(word)
print(result)

# Q32. Given a list and target, find two numbers whose sum equals the target using a dictionary.
numbers = [2, 7, 11, 15, 3, 6]
target = 9
seen = {}
for num in numbers:
    if target - num in seen:
        print("Pair:", target - num, num)
        break
    seen[num] = True

