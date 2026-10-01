# QUESTION 6
# Create a dictionary containing Student_ID, Name, Department,
# Total_Classes and Classes_Attended.
# Calculate:
# Attendance Percentage = (Classes_Attended / Total_Classes) × 100
# Display students whose attendance is below 75%.
# ============================================================

attendance = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE"],
    "Total_Classes": [100, 100, 90, 80, 100],
    "Classes_Attended": [80, 70, 85, 55, 92]
}

df = pd.DataFrame(attendance)

print("\nQUESTION 6")

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# ============================================================
