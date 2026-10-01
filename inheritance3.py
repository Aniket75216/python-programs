# Student multiple inheritance

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        return sum(self.marks) + self.points


student = Student([80, 75, 85], 20)

print("Academic Marks:", student.marks)
print("Sports Points:", student.points)
print("Overall Performance:", student.performance())\n