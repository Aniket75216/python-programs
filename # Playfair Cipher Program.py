# Playfair Cipher Program

def generate_key_table(key):
    key = key.upper().replace("J", "I")
    table = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            table.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":   # J is omitted
        if ch not in used:
            table.append(ch)
            used.add(ch)

    return [table[i:i+5] for i in range(0, 25, 5)]


def find_position(table, ch):
    if ch == "J":
        ch = "I"
    for i in range(5):
        for j in range(5):
            if table[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1
    return result


def encrypt(text, table):
    cipher = ""
    text = prepare_text(text)

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2:  # Same row
            cipher += table[r1][(c1 + 1) % 5]
            cipher += table[r2][(c2 + 1) % 5]
        elif c1 == c2:  # Same column
            cipher += table[(r1 + 1) % 5][c1]
            cipher += table[(r2 + 1) % 5][c2]
        else:  # Rectangle
            cipher += table[r1][c2]
            cipher += table[r2][c1]

    return cipher


# Main Program
key = input("Enter the key: ")
message = input("Enter the message: ")

table = generate_key_table(key)

print("\nKey Matrix:")
for row in table:
    print(" ".join(row))

cipher = encrypt(message, table)
print("\nEncrypted Message:", cipher)