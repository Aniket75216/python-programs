# Create a nested tuple containing student details

students = (
    (101, "Rahul", 85),
    (102, "Amit", 90),
    (103, "Sneha", 88),
    (104, "Priya", 92)
)

for student in students:
    print("ID:", student[0], "Name:", student[1], "Marks:", student[2])

# Store ten numbers in a tuple and calculate their sum

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = 0

for num in numbers:
    total = total + num

print("Sum =", total)

# Find the largest and smallest number in a tuple

numbers = (25, 10, 45, 5, 60, 30)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

# Calculate the average of elements stored in a tuple

numbers = (10, 20, 30, 40, 50)

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Average =", average)