# Multiple and hierarchical inheritance

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def study(self):
        print(self.name, "is studying")


class Faculty(Person):
    def teach(self):
        print(self.name, "is teaching")


class TeachingAssistant(Student, Faculty):
    def work(self):
        self.study()
        self.teach()


assistant = TeachingAssistant("Amit")
assistant.work()\n