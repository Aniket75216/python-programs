nums = [12, 15, 20, 33, 40, 55, 60, 77, 80, 91, 22, 11, 44, 99, 100]

even = 0
odd = 0

for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)