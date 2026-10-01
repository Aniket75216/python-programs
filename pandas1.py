# QUESTION 1
# Create a dictionary containing information for 5 students:
# Student ID, Student Name, Python Marks, DBMS Marks,
# Mathematics Marks.
# Convert it into a Pandas DataFrame and:
# 1. Display the DataFrame.
# 2. Calculate total marks for each student.
# 3. Calculate average marks.
# 4. Display students who scored more than 75% average.
# ============================================================

students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit"],
    "Python": [80, 72, 90, 65, 85],
    "DBMS": [75, 80, 88, 70, 92],
    "Mathematics": [85, 78, 95, 68, 80]
}

df = pd.DataFrame(students)

print("\nQUESTION 1")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df[["Student_ID", "Student_Name", "Total", "Average"]])

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])


# ============================================================
