# ============================================================
# PYTHON DICTIONARY PROGRAMS - 35 QUESTIONS
# ============================================================

# Q1. Create a dictionary containing student details and display all key-value pairs.
student = {"roll_no": 101, "name": "Rahul", "department": "Computer Science", "marks": 85}
for key, value in student.items():
    print(key, ":", value)

# Q2. Create employee information and display the value associated with a specified key.
employee = {"id": 101, "name": "Amit", "department": "IT", "salary": 55000}
key = input("Enter employee key: ")
print(employee.get(key, "Key not found"))

# Q3. Create a dictionary of five products and add a new product and price.
products = {"Pen": 10, "Book": 50, "Bag": 500, "Pencil": 5, "Bottle": 100}
products["Eraser"] = 8
print(products)

# Q4. Create student marks dictionary and update marks of a specified student.
marks = {"Rahul": 80, "Amit": 75, "Sneha": 90}
name = input("Enter student name: ")
marks[name] = int(input("Enter new marks: "))
print(marks)

# Q5. Create cities and populations dictionary and remove a specified city.
cities = {"Mumbai": 20000000, "Delhi": 19000000, "Pune": 7000000}
city = input("Enter city to remove: ")
cities.pop(city, None)
print(cities)

# Q6. Create employee IDs and names dictionary and check whether an ID exists.
employees = {101: "Rahul", 102: "Amit", 103: "Sneha"}
emp_id = int(input("Enter employee ID: "))
print("Exists" if emp_id in employees else "Does not exist")

# Q7. Create student records and find the total number of key-value pairs.
students = {"Rahul": 85, "Amit": 78, "Sneha": 92}
print("Total:", len(students))

# Q8. Create a dictionary and display all keys, values and key-value pairs.
data = {"name": "Rahul", "age": 20, "course": "BCA"}
print("Keys:", data.keys())
print("Values:", data.values())
print("Items:", data.items())

# Q9. Create programming languages and creators dictionary and display using a loop.
languages = {"Python": "Guido van Rossum", "Java": "James Gosling", "C": "Dennis Ritchie"}
for language, creator in languages.items():
    print(language, ":", creator)

