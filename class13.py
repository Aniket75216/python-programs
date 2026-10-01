# Student result with constructor and destructor

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 35:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed.")


student = StudentResult("Amit", [80, 75, 85, 90, 78])

student.display()

del student
