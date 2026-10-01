# QUESTION 11
# Create a Pandas Series using a dictionary containing
# student names and attendance percentages.
# Perform:
# 1. Find average attendance.
# 2. Display students with attendance below 75%.
# 3. Display students with attendance above 90%.
# 4. Find highest attendance.
# ============================================================

student_attendance = {
    "Amit": 80,
    "Rahul": 70,
    "Sneha": 95,
    "Priya": 68,
    "Rohit": 92
}

series = pd.Series(student_attendance)

print("\nQUESTION 11")
print(series)

print("\nAverage Attendance:")
print(series.mean())

print("\nStudents below 75%:")
print(series[series < 75])

print("\nStudents above 90%:")
print(series[series > 90])

print("\nHighest Attendance:")
print(series.max())


# ============================================================
