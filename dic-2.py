# Q10. Accept five student names and marks and store them in a dictionary.
students = {}
for i in range(5):
    name = input("Enter student name: ")
    students[name] = float(input("Enter marks: "))
print(students)

# Q11. Create student marks dictionary and find the student with highest marks.
students = {"Rahul": 85, "Amit": 92, "Sneha": 88, "Priya": 95}
name = max(students, key=students.get)
print("Highest:", name, students[name])

# Q12. Create student marks dictionary and find the student with lowest marks.
students = {"Rahul": 85, "Amit": 72, "Sneha": 88, "Priya": 95}
name = min(students, key=students.get)
print("Lowest:", name, students[name])

# Q13. Create student marks dictionary and calculate average marks.
students = {"Rahul": 85, "Amit": 72, "Sneha": 88, "Priya": 95}
print("Average:", sum(students.values()) / len(students))

# Q14. Accept a string and create a dictionary containing each character and its frequency.
text = input("Enter string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

# Q15. Accept a sentence and create a dictionary containing each word and its frequency.
sentence = input("Enter sentence: ").split()
frequency = {}
for word in sentence:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)

# Q16. Create two dictionaries and merge them into a single dictionary.
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
dict1.update(dict2)
print(dict1)

# Q17. Given two dictionaries, find the keys that are common to both.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}
print("Common keys:", dict1.keys() & dict2.keys())

# Q18. Given two dictionaries, identify the values that are common to both.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 40, "z": 30}
print("Common values:", set(dict1.values()) & set(dict2.values()))

