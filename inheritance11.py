# Student result inheritance

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()
        if p >= 75:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 50:
            return "C"
        return "D"


result = Result(101, "Amit", "B.Tech", [80, 75, 85])

print("Total:", result.total())
print("Percentage:", result.percentage())
print("Grade:", result.grade())\n