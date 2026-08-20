# Q19. Create a dictionary with duplicate values and remove duplicate values.
data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)

# Q20. Create a dictionary and display its elements in ascending order of keys.
data = {5: "E", 2: "B", 4: "D", 1: "A", 3: "C"}
for key in sorted(data):
    print(key, ":", data[key])

# Q21. Create a dictionary containing numbers from 1 to 10 and their squares.
squares = {i: i ** 2 for i in range(1, 11)}
print(squares)

# Q22. Create a dictionary containing even numbers from 1 to 20 and their squares.
squares = {i: i ** 2 for i in range(2, 21, 2)}
print(squares)

# Q23. Given a list of numbers, create a dictionary containing each unique number and its frequency.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)

# Q24. Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {i: i ** 3 for i in range(1, 11)}
print(cubes)

# Q25. Create a student management program for add, update, delete, search, display, highest and average.
students = {"Rahul": 85, "Amit": 78, "Sneha": 92}
while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Display 6.Highest 7.Average 8.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        students[input("Name: ")] = float(input("Marks: "))
    elif choice == 2:
        name = input("Name: ")
        if name in students:
            students[name] = float(input("New marks: "))
    elif choice == 3:
        students.pop(input("Name: "), None)
    elif choice == 4:
        print(students.get(input("Name: "), "Not found"))
    elif choice == 5:
        print(students)
    elif choice == 6:
        name = max(students, key=students.get)
        print(name, students[name])
    elif choice == 7:
        print(sum(students.values()) / len(students))
    elif choice == 8:
        break

