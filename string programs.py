#Write a program to input a string and display its length without using the len() function. 
text=input("Enter a string :")
count=0
for ch in text:
    count+=1
print("the length of the string is :",count)

#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
text=input("Enter a string :")
vowels=0
consonants=0
digits=0
spaces=0
specialch=0
for ch in text:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else:
        specialch+=1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", specialch)

#Reverse the given string without using built-in reverse functions. 
a=input("Enter a string :")
reverse=""
for ch in a:
    reverse=ch + reverse
print("The reversed string is :",reverse)

#Check whether the entered string is a palindrome. 
text=input("Enter a string :")
if text==text[::-1]:
    print(text ,"is a palindrome")
else:
    print(text ,"is not a palindrome")
