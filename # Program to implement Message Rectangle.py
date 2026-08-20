# Program to implement Message Rectangle Technique for Transposition Cipher

message = input("Enter the message: ").replace(" ", "")
cols = int(input("Enter the number of columns: "))

# Calculate number of rows
rows = len(message) // cols
if len(message) % cols != 0:
    rows += 1

# Fill the rectangle row-wise
matrix = []
index = 0

for i in range(rows):
    row = []
    for j in range(cols):
        if index < len(message):
            row.append(message[index])
            index += 1
        else:
            row.append('X')   # Padding character
    matrix.append(row)

print("\nMessage Rectangle:")
for row in matrix:
    print(" ".join(row))

# Read column-wise to get ciphertext
cipher = ""

for j in range(cols):
    for i in range(rows):
        cipher += matrix[i][j]

print("\nEncrypted Message:", cipher)