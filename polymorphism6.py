# Student grade polymorphism

class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 75 else "B"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 70 else "B"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        return "A" if marks >= 65 else "B"


for student in [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]:
    print(student.calculate_grade(72))\n