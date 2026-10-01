# Medical multiple and hierarchical inheritance

class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def treat(self):
        print(self.name, "treats patients")


class Patient(Person):
    def visit(self):
        print(self.name, "visits hospital")


class Surgeon(Doctor):
    def surgery(self):
        print(self.name, "performs surgery")


class MedicalResearcher(Doctor):
    def research(self):
        print(self.name, "does medical research")


Surgeon("Dr. Amit").surgery()
MedicalResearcher("Dr. Rahul").research()
Patient("Sneha").visit()\n