# Replace a word in a text file

filename = input("Enter file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open(filename, "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open(filename, "w") as file:
    file.write(text)

print("Word replaced successfully.")\n