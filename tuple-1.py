# Create a tuple of five integers and display it

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

# Create a tuple containing five city names and display first, last and third city

cities = ("Pune", "Mumbai", "Delhi", "Chennai", "Bangalore")

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])

# Create a tuple of student names and display the total number of students

students = ("Rahul", "Amit", "Sneha", "Priya", "Rohit")

print("Students:", students)
print("Total number of students:", len(students))

# Create a tuple of colors and check whether a given color exists

colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter a color: ")

if color in colors:
    print("Color exists in the tuple.")
else:
    print("Color does not exist in the tuple.")

# Create a tuple of fruits and display each fruit using a loop

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)

# Create a tuple with repeated numbers and count how many times a particular number appears

numbers = (10, 20, 10, 30, 10, 40, 20, 10)

num = int(input("Enter a number: "))

count = numbers.count(num)

print("Number of times", num, "appears:", count)