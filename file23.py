# Compare two text files

file1 = input("Enter first file: ")
file2 = input("Enter second file: ")

with open(file1, "r") as first:
    lines1 = first.readlines()

with open(file2, "r") as second:
    lines2 = second.readlines()

if lines1 == lines2:
    print("Files are identical.")
else:
    print("Files are different.")

    for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        if line1 != line2:
            print("First difference at line:", i)
            break\n