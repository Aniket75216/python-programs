# Store item prices in a tuple and calculate total, average, highest and lowest price

prices = (50, 120, 80, 200, 150, 90)

total = 0
highest = prices[0]
lowest = prices[0]

for price in prices:
    total = total + price

    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

average = total / len(prices)

print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)

# Store temperatures of seven days and calculate maximum, minimum and average

temperatures = (32, 35, 31, 34, 36, 33, 30)

total = 0
maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    total = total + temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)