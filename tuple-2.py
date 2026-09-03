# Create a tuple of employee IDs and find the index of a given ID

employee_ids = (101, 102, 103, 104, 105)

id = int(input("Enter employee ID: "))

if id in employee_ids:
    print("Index of", id, "is:", employee_ids.index(id))
else:
    print("Employee ID not found.")

# Create two tuples of numbers and concatenate them

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)

result = tuple1 + tuple2

print("First tuple:", tuple1)
print("Second tuple:", tuple2)
print("Concatenated tuple:", result)

# Create a tuple containing three elements and repeat it four times

t = (10, 20, 30)

result = t * 4

print("Repeated tuple:", result)

# Create a tuple of 10 numbers and display different parts

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five elements:", numbers[:5])

print("Last five elements:", numbers[5:])

print("Middle four elements:", numbers[3:7])

print("Alternate elements:", numbers[::2])

print("Reverse tuple:", numbers[::-1])

