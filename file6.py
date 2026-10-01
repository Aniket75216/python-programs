# Count total words in a text file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read()

words = text.split()

print("Total number of words:", len(words))\n