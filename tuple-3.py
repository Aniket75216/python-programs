# Convert a tuple into a list and add a new element

fruits = ("Apple", "Banana", "Mango")

fruit_list = list(fruits)

fruit_list.append("Orange")

fruits = tuple(fruit_list)

print("Updated tuple:", fruits)

# Accept five numbers and convert the list into a tuple

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers = tuple(numbers)

print("Tuple:", numbers)

# Modify a tuple by converting it into a list and then back into a tuple

numbers = (10, 20, 30, 40)

print("Original tuple:", numbers)

numbers_list = list(numbers)

numbers_list[1] = 200

numbers = tuple(numbers_list)

print("Modified tuple:", numbers)

# Create a tuple and delete it completely

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

del numbers

print("Tuple deleted successfully.")