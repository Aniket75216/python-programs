# Process student records from a file

filename = "students.txt"

records = [
    "101,Amit,85",
    "102,Priya,92",
    "103,Rahul,78"
]

with open(filename, "w") as file:
    for record in records:
        file.write(record + "\n")

students = []

with open(filename, "r") as file:
    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((int(roll), name, float(marks)))

print("All Records:")
for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])
average = sum(student[2] for student in students) / len(students)

print("\nHighest Marks:")
print(highest)

print("\nAverage Marks:", average)

print("\nStudents scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student)\n