nums = []

for i in range(10):
    n = int(input("Enter number: "))
    nums.append(n)

total = sum(nums)
avg = total / 10

print("Sum =", total)
print("Average =", avg)