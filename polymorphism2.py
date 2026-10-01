# Employee salary polymorphism

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000


class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 8000


class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 5000


for employee in [Manager(), Developer(), Tester()]:
    print("Salary:", employee.calculate_salary())\n