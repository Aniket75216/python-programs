# Count vowels and consonants in a text file

filename = input("Enter file name: ")

with open(filename, "r") as file:
    text = file.read().lower()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)\n