# Student comparison operator overloading

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Amit", 85)
s2 = Student("Rahul", 78)

print("Amit > Rahul:", s1 > s2)
print("Amit < Rahul:", s1 < s2)\n