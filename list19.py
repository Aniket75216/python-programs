students = ["Amit", "Ravi", "Neha"]

print("Total Students:", len(students))

name = input("Enter name to search: ")

if name in students:
    print("Present")
else:
    print("Absent")

students.append("Pooja")
students.remove("Ravi")

print(students)