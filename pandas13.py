# QUESTION 13
# Dataset: employees.csv
# Columns:
# Employee_ID, Name, Department, Experience, Salary
#
# Read the CSV file and:
# 1. Display employees from the CSE department.
# 2. Find average salary.
# 3. Find highest and lowest salary.
# 4. Display employees having salary greater than 50,000.
# 5. Calculate department-wise average salary.
# ============================================================

df = pd.read_csv("employees.csv")

print("\nQUESTION 13")

print("\nEmployees from CSE department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees having salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise average salary:")
print(df.groupby("Department")["Salary"].mean())


# ============================================================
