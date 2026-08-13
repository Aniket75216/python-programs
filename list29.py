temp = [30,31,29,28,35,36,34,32,33,31,
        30,29,28,37,38,36,35,34,33,32,
        31,30,29,28,35,36,34,33,32,31]

avg = sum(temp)/len(temp)

print("Hottest Day =", max(temp))
print("Coldest Day =", min(temp))
print("Average Temperature =", avg)

above = 0
below = 0

for t in temp:
    if t > avg:
        above += 1
    elif t < avg:
        below += 1

print("Days Above Average =", above)
print("Days Below Average =", below)