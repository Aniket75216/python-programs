# Search a word and display occurrences with line numbers

filename = input("Enter file name: ")
search_word = input("Enter word to search: ").lower()

count = 0
lines_found = []

with open(filename, "r") as file:
    for line_no, line in enumerate(file, start=1):
        words = line.lower().split()
        occurrences = words.count(search_word)

        if occurrences > 0:
            count += occurrences
            lines_found.append(line_no)

print("Occurrences:", count)
print("Line numbers:", lines_found)\n