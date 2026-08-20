# Q17. Two students have selected different subjects.
# Find the subjects studied by both students.
student1 = {"Python", "Java", "DBMS", "OS"}
student2 = {"Java", "DBMS", "CN", "AI"}

common_subjects = student1.intersection(student2)

print("\nQ17. Subjects studied by both students:", common_subjects)


# Q18. Accept a sentence from the user
# and use a set to display all unique words.
sentence = input("\nQ18. Enter a sentence: ")

words = set(sentence.split())

print("Unique words:")
for word in words:
    print(word)


# Q19. Students present in morning and afternoon sessions.
morning = {"Amit", "Rahul", "Sneha", "Priya", "Rohan"}
afternoon = {"Sneha", "Priya", "Kiran", "Neha", "Rohan"}

both = morning.intersection(afternoon)
only_morning = morning.difference(afternoon)
only_afternoon = afternoon.difference(morning)
at_least_one = morning.union(afternoon)

print("\nQ19. Students present in both sessions:", both)
print("Students only in morning:", only_morning)
print("Students only in afternoon:", only_afternoon)
print("Students present in at least one session:", at_least_one)


# Q20. Create sets representing students enrolled in Python and Java.
python_students = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
java_students = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

print("\nQ20. Python students:", python_students)
print("Java students:", java_students)


# Q21. Find students enrolled in both courses
# and students enrolled in only one course.
python_students = {"Amit", "Rahul", "Sneha", "Priya", "Kiran"}
java_students = {"Sneha", "Priya", "Rohan", "Neha", "Kiran"}

both = python_students.intersection(java_students)
only_one = python_students.symmetric_difference(java_students)

print("\nQ21. Students enrolled in both courses:", both)
print("Students enrolled in only one course:", only_one)


