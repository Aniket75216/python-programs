# Program to print the first and last character of a string

text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])

# Program to display each character and its ASCII value

text = input("Enter a string: ")

for ch in text:
    print(ch, "=", ord(ch))

#Count the total number of words in a sentence. 
text=input("Enter a sentence:")
words=text.split()
print("total number of words =",len(words))

# Program to find the longest word in a sentence
text = input("Enter a sentence: ")

words = text.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length:", len(longest))

#Find the shortest word in a sentence. 
text = input("Enter a sentence: ")

words = text.split()

smallest = words[0]

for word in words:
    if len(word) < len(smallest):
        smallest = word

print("smallest word:", smallest)
print("Length:", len(smallest))

# Program to convert the first letter of every word to uppercase

text = input("Enter a sentence: ")

result = text.title()

print("Modified sentence:", result)
