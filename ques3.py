import csv

# Store employee records in CSV file
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["ID", "Name", "Department", "Salary"])

    n = int(input("Enter number of employees: "))

    for i in range(n):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        writer.writerow([emp_id, name, department, salary])

# Display employees above given salary
given_salary = float(input("\nEnter salary limit: "))

print("\nEmployees earning above", given_salary, ":")

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        if float(employee["Salary"]) > given_salary:
            print(employee["ID"],
                  employee["Name"],
                  employee["Department"],
                  employee["Salary"])