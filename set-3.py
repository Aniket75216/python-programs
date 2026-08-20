# Q12. Find elements present in either set but not in both.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.symmetric_difference(set2)

print("\nQ12. Elements in either set but not both:", result)


# Q13. Determine whether first set is a subset of second set.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("\nQ13. First set is a subset of second set.")
else:
    print("\nQ13. First set is not a subset of second set.")


# Q14. Determine whether first set is a superset of second set.
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

if set1.issuperset(set2):
    print("\nQ14. First set is a superset of second set.")
else:
    print("\nQ14. First set is not a superset of second set.")


# Q15. Determine whether two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("\nQ15. The sets have no elements in common.")
else:
    print("\nQ15. The sets have elements in common.")


# Q16. Create two sets and check whether they are equal.
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

if set1 == set2:
    print("\nQ16. Both sets are equal.")
else:
    print("\nQ16. Both sets are not equal.")


