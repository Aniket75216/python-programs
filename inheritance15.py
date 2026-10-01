# Research student inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(self.name, self.age, self.roll_no, self.course)
        print(self.topic, self.guide)


student = ResearchStudent(
    "Amit", 23, 101, "B.Tech", "Machine Learning", "Dr. Sharma"
)
student.display()\n