# Count the frequency of each element in a tuple

numbers = (10, 20, 10, 30, 20, 10, 40, 30)

checked = ()

for item in numbers:
    if item not in checked:
        print(item, "appears", numbers.count(item), "times")
        checked = checked + (item,)

# Convert a tuple into sorted tuples in ascending and descending order

numbers = (50, 10, 40, 20, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Original tuple:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)

# Create a tuple containing patient records

patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Amit", 22, "O+"),
    (104, "Priya", 28, "A+"),
    (105, "Rohit", 35, "O-")
)

# 1. Display all records
print("All Patient Records:")
for patient in patients:
    print("Patient ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Blood Group:", patient[3])
    print("----------------------")


