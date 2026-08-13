nums = [1, 2, 2, 3, 4, 3, 5, 1]

result = []

for i in nums:
    if i not in result:
        result.append(i)

print(result)