# Create student.txt and write student details

with open("student.txt", "w") as file:
    file.write("Name: Amit\n")
    file.write("Roll Number: 101\n")
    file.write("Branch: CSE\n")
    file.write("Semester: 5\n")

print("Student details written successfully.")\n