# ============================================================
# SET PROGRAMS - Q1 TO Q25
# ============================================================


# Q1. Create a set containing five integers and display all its elements.
numbers = {10, 20, 30, 40, 50}

print("Q1. Set elements:")
for i in numbers:
    print(i)


# Q2. Create a list containing duplicate values.
# Convert the list into a set and display the resulting set.
numbers = [10, 20, 10, 30, 20, 40]

result = set(numbers)

print("\nQ2. Original list:", numbers)
print("Resulting set:", result)


# Q3. Create a set of five fruits.
# Add two new fruits and display the updated set.
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print("\nQ3. Updated fruits set:", fruits)


# Q4. Create a set of numbers and remove a specified number.
numbers = {10, 20, 30, 40, 50}

num = 30
numbers.remove(num)

print("\nQ4. Set after removing", num, ":", numbers)


# Q5. Create a set of student names.
# Ask the user to enter a name and check whether the student exists.
students = {"Amit", "Rahul", "Sneha", "Priya", "Rohan"}

name = input("\nQ5. Enter student name: ")

if name in students:
    print(name, "exists in the set.")
else:
    print(name, "does not exist in the set.")


