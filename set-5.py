# Q22. Technical skills of two employees.
employee1 = {"Python", "Java", "SQL", "Git", "HTML"}
employee2 = {"Python", "C++", "SQL", "Docker", "Git"}

common_skills = employee1.intersection(employee2)
unique_employee1 = employee1.difference(employee2)
unique_employee2 = employee2.difference(employee1)
all_skills = employee1.union(employee2)

print("\nQ22. Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)


# Q23. Available books and requested books.
available_books = {
    "Python Basics",
    "Java Programming",
    "Data Structures",
    "DBMS"
}

requested_books = {
    "Python Basics",
    "DBMS",
    "Operating Systems",
    "AI Basics"
}

available_requested = available_books.intersection(requested_books)

print("\nQ23. Requested books that are available:")
print(available_requested)


# Q24. Visitor IDs from two different days.
day1 = {101, 102, 103, 104, 105}
day2 = {104, 105, 106, 107, 108}

unique_visitors = day1.union(day2)
returning_visitors = day1.intersection(day2)
only_first_day = day1.difference(day2)
only_second_day = day2.difference(day1)

print("\nQ24. Unique visitors across both days:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", only_first_day)
print("Visitors only on second day:", only_second_day)


