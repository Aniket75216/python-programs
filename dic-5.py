# Q33. Take a string and find the first character that occurs only once.
text = input("Enter string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
for char in text:
    if frequency[char] == 1:
        print("First non-repeating:", char)
        break

# Q34. Take a string and find the first character that occurs more than once.
text = input("Enter string: ")
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
for char in text:
    if frequency[char] > 1:
        print("First repeating:", char)
        break

# Q35. Accept a paragraph and create a dictionary of word length and number of words.
paragraph = input("Enter paragraph: ")
words = paragraph.split()
length_count = {}
for word in words:
    word = word.strip(".,!?;:")
    if word:
        length_count[len(word)] = length_count.get(len(word), 0) + 1
print(length_count)