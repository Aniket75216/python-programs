# QUESTION 8
# Create a Pandas Series using a dictionary containing
# employee names and their salaries.
# Perform:
# 1. Find highest salary.
# 2. Find lowest salary.
# 3. Calculate average salary.
# 4. Display employees earning more than 50,000.
# ============================================================

employee_salary = {
    "Amit": 55000,
    "Rahul": 48000,
    "Sneha": 72000,
    "Priya": 45000,
    "Rohit": 65000
}

series = pd.Series(employee_salary)

print("\nQUESTION 8")
print(series)

print("\nHighest Salary:")
print(series.max())

print("\nLowest Salary:")
print(series.min())

print("\nAverage Salary:")
print(series.mean())

print("\nEmployees earning more than 50000:")
print(series[series > 50000])


# ============================================================
