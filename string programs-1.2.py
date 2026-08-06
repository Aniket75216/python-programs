#Count the number of uppercase and lowercase letters in a string. 
text=input("Enter a string :")
lower=0
upper=0
for ch in text:
    if ch.islower():
        lower+=1
    elif ch.isupper():
        upper+=1
print("lower case count =",lower)
print("upper case count =",upper)

#Replace all occurrences of a given character with another character. 
# Program to replace all occurrences of a character

text = input("Enter a string: ")
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")

result = ""

for ch in text:
    if ch == old:
        result += new
    else:
        result += ch

print("Modified string:", result)

#Remove all spaces from the input string. 
# Program to remove all spaces from a string

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("String without spaces:", result)

#Find the number of times a specified character appears in a string. 
text=input("Enter a string")
input=input("Enter a character to count")
count=0
for ch in text:
    if ch==input:
        count+=1
print("number of occurences",count)