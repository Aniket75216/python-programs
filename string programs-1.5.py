#Count how many times a specific word appears in a sentence. 
text=input("Enter a string :")
word=input("enter a word to count :")
count=0
words=text.split()
count=words.count(word)
print("number of ", word,"word is",count)

# Program to validate a password based on given conditions

import string

password = input("Enter password: ")

if (len(password) >= 8 and
    any(ch.isupper() for ch in password) and
    any(ch.islower() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(ch in string.punctuation for ch in password)):
    print("Valid Password")
else:
    print("Invalid Password")

# Program to compress a string using Run-Length Encoding

s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print("Compressed String:", result)

# Program to compress a string and return the original if compression is not shorter

s = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        compressed += s[i] + str(count)
        count = 1

if len(compressed) < len(s):
    print("Compressed String:", compressed)
else:
    print("Original String:", s)