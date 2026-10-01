# QUESTION 12
# Dataset: students.csv
# Columns:
# Student_ID, Name, Department, Python, DBMS, Maths
#
# Read students.csv using Pandas and perform:
# 1. Display first 5 records.
# 2. Display last 5 records.
# 3. Find total and average marks of each student.
# 4. Display students whose average marks are greater than 75.
# 5. Find student with highest average.
# 6. Find average marks for each subject.
# ============================================================

df = pd.read_csv("students.csv")

print("\nQUESTION 12")

print("\nFirst 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nTotal and Average marks:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())


# ============================================================
