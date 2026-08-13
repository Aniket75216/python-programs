nums = [15, 8, 25, 3, 18]

largest = nums[0]
smallest = nums[0]

for i in nums:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest =", largest)
print("Smallest =", smallest)