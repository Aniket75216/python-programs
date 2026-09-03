# Store runs scored in 10 matches and calculate total, highest, lowest and average

runs = (45, 72, 30, 90, 55, 110, 65, 40, 85, 50)

total = 0
highest = runs[0]
lowest = runs[0]

for run in runs:
    total = total + run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

average = total / len(runs)

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)

# Create two tuples and find the common elements

tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for item in tuple1:
    if item in tuple2:
        common = common + (item,)

print("Common elements:", common)

# Merge two tuples and remove duplicate elements

tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

result = ()

for item in merged:
    if item not in result:
        result = result + (item,)

print("Merged tuple:", merged)
print("After removing duplicates:", result)