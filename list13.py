nums = []

for i in range(10):
    n = int(input("Enter number: "))
    nums.append(n)

nums.sort()
print("Ascending:", nums)

nums.sort(reverse=True)
print("Descending:", nums)