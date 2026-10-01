# Find the longest word in a text file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    words = file.read().split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("File is empty.")\n