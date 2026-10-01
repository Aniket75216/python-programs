# QUESTION 2
# Create a dictionary containing Employee ID, Employee Name,
# Department, Salary and Experience.
# Convert it into a Pandas DataFrame and:
# 1. Display employees with salary greater than 50,000.
# 2. Find the average salary.
# 3. Find the highest salary.
# 4. Find the employee with the highest experience.
# ============================================================

employees = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Raj", "Neha", "Amit", "Sneha", "Vijay"],
    "Department": ["CSE", "IT", "CSE", "HR", "IT"],
    "Salary": [55000, 48000, 72000, 45000, 65000],
    "Experience": [3, 2, 6, 4, 8]
}

df = pd.DataFrame(employees)

print("\nQUESTION 2")
print(df)

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])


# ============================================================
