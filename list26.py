marks = [45,67,89,56,78,90,34,65,77,88,
         55,66,99,44,73,81,62,58,69,92]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest =", highest)
print("Lowest =", lowest)
print("Average =", average)
print("Above Average =", above)
print("Below Average =", below)