# Q6. Create a set of cities and determine the total number of cities.
cities = {"Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur"}

print("\nQ6. Total number of cities:", len(cities))


# Q7. Create a set of programming languages
# and display each language using a for loop.
languages = {"Python", "Java", "C++", "JavaScript", "Dart"}

print("\nQ7. Programming languages:")
for language in languages:
    print(language)


# Q8. Create a list containing duplicate numbers.
# Use a set to remove the duplicates.
numbers = [10, 20, 10, 30, 40, 20, 50, 30]

unique_numbers = set(numbers)

print("\nQ8. Original list:", numbers)
print("After removing duplicates:", unique_numbers)


# Q9. Create two sets of integers and find their union.
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

union_set = set1.union(set2)

print("\nQ9. Union:", union_set)


# Q10. Create two sets and find the elements common to both sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

print("\nQ10. Common elements:", common)


# Q11. Find:
# Elements present in first set but not second
# Elements present in second set but not first
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

only_first = set1.difference(set2)
only_second = set2.difference(set1)

print("\nQ11. Elements only in first set:", only_first)
print("Elements only in second set:", only_second)


