#Write a PYTHON program to produce following designA B C A B C A B C 
for i in range(3):
    for j in range(65, 68):
        print(chr(j), end=" ")
    print()

#9.  Write a PYTHON program to produce following design
#      A
#     A B
#    A B C
#      A B C D 
#      A B C D E
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#. Write a PYTHON program to produce following design
#       A B C D E
#       A B C D
#       A B C
#       A B
#       A                      
n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#11. Write a PYTHON program to produce following  
#      design
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#12. Write a PYTHON program to produce following design
#     1
#      2 2
#      3 3 3
#      4 4 4 4 
#      5 5 5 5 5
n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
