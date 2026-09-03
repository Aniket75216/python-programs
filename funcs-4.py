# 11. Second Largest
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

numbers = [10, 50, 20, 40, 30]
print("Second largest =", second_largest(numbers))


# 12. First n Fibonacci Numbers
def fibonacci(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter n: "))
print("Fibonacci =", fibonacci(n))


# 13. Percentage and Grade
def percentage_grade(marks):
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

    return percentage, grade

marks = []
for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = percentage_grade(marks)
print("Percentage =", percentage)
print("Grade =", grade)
