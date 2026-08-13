nums = [10, 20, 30, 40, 50]

left = nums[1:] + [nums[0]]
right = [nums[-1]] + nums[:-1]

print("Left Rotation :", left)
print("Right Rotation:", right)