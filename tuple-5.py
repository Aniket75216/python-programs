# Store 15 integers in a tuple and count even and odd numbers

numbers = (1, 2, 5, 8, 10, 13, 16, 21, 24, 27, 30, 33, 36, 40, 45)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# Accept a number from the user and check whether it exists in the tuple

numbers = (10, 20, 30, 40, 50)

num = int(input("Enter a number: "))

if num in numbers:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")

# Store student details in a tuple and display all details

student = (101, "Rahul", "Computer Engineering", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])

# Create tuples containing employee ID, name and salary

employees = (
    (101, "Amit", 35000),
    (102, "Sneha", 40000),
    (103, "Rahul", 45000),
    (104, "Priya", 38000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print("--------------------")