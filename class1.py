# Student class

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)
        print()

students = [
    Student(1, "Amit", [80, 75, 85]),
    Student(2, "Rahul", [70, 82, 78]),
    Student(3, "Sneha", [90, 88, 92])
]

for student in students:
    student.display()
