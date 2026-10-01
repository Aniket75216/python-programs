# Process employee records from a file

filename = "employees.txt"

records = [
    "101,Amit,CSE,55000",
    "102,Rahul,IT,48000",
    "103,Sneha,HR,72000"
]

with open(filename, "w") as file:
    for record in records:
        file.write(record + "\n")

employees = []

with open(filename, "r") as file:
    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append((int(emp_id), name, department, float(salary)))

def display_employees():
    for employee in employees:
        print(employee)

def highest_paid():
    return max(employees, key=lambda x: x[3])

def average_salary():
    return sum(employee[3] for employee in employees) / len(employees)

def above_salary(amount):
    for employee in employees:
        if employee[3] > amount:
            print(employee)

print("All Employees:")
display_employees()

print("\nHighest Paid:")
print(highest_paid())

print("\nAverage Salary:", average_salary())

print("\nEmployees above 50000:")
above_salary(50000)\n