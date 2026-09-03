# 40. filter() - Words More Than Five Characters
words = ["apple", "banana", "cat", "elephant", "dog"]
result = list(filter(lambda x: len(x) > 5, words))
print("Words > 5 characters =", result)


# 41. Sort Words According to Length
words = ["apple", "cat", "elephant", "dog", "banana"]
words.sort(key=lambda x: len(x))
print("Sorted words =", words)


# 42. Sort Students According to Marks
students = [
    ("Aniket", 85),
    ("Rahul", 70),
    ("Amit", 92),
    ("Rohit", 78)
]

students.sort(key=lambda x: x[1])
print("Students sorted by marks =", students)


# 43. Sort Employees According to Salary
employees = [
    ("Aniket", 50000),
    ("Rahul", 40000),
    ("Amit", 70000),
    ("Rohit", 60000)
]

employees.sort(key=lambda x: x[1])
print("Employees sorted by salary =", employees)


# 44. Students - Average, Filter and Sort
students = [
    ("Aniket", 85),
    ("Rahul", 65),
    ("Amit", 92),
    ("Rohit", 72)
]

average = sum(map(lambda x: x[1], students)) / len(students)
above_75 = list(filter(lambda x: x[1] > 75, students))
sorted_students = sorted(students, key=lambda x: x[1])

print("Average =", average)
print("Above 75 =", above_75)
print("Sorted =", sorted_students)


