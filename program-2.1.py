a=int(input("enter a number "))
b=int(input("enter another number "))
c=int(input("enter another number "))
if(a>b):
    if(a>c):
        print(a,"is the largest ")
    else:
        print(c,"is the largest ")
elif(b>c):
    print(b,"is the largest ")      
else:
    print(c,"is the largest ") 