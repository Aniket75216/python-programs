scores = [45,120,65,89,150,30,75,102,48,60]

print("Highest Score =", max(scores))
print("Lowest Score =", min(scores))
print("Total Runs =", sum(scores))
print("Average Runs =", sum(scores)/len(scores))

century = 0
half_century = 0

for s in scores:
    if s >= 100:
        century += 1
    elif s >= 50:
        half_century += 1

print("Centuries =", century)
print("Half Centuries =", half_century)