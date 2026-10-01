# Count frequency of each word using dictionary

filename = input("Enter file name: ")

with open(filename, "r") as file:
    words = file.read().lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)\n