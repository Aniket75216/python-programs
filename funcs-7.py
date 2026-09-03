# 18. Student Records
def calculate_marks(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = []

    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total, percentage, grade = calculate_marks(marks)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

class_average = sum(s["percentage"] for s in students) / n
highest = students[0]
lowest = students[0]

for s in students:
    if s["percentage"] > highest["percentage"]:
        highest = s
    if s["percentage"] < lowest["percentage"]:
        lowest = s

for s in students:
    print("\nName:", s["name"])
    print("Roll:", s["roll"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"])
    print("Grade:", s["grade"])

print("\nClass Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])


