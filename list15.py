nums = [10, 50, 30, 80, 60]

largest = second = nums[0]

for i in nums:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)