num=int(input("enter the number:"))
temp=num
rev=0
while temp>0:
    rev=rev*10+(temp%10)
    temp=temp//10
if num==rev:
    print("is palindrome")
else:
    print("Not a palindrome")       