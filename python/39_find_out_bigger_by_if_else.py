#write a program to find out elder brother from given two brother's age. 

import sys

brother1=int(input("enter age of person one(1) ..."))
print(brother1)
brother2=int(input("enter age of person two(2)..."))
print(brother2)

if brother1==brother2:
    print("both have same age!!!")
    sys.exit()
if brother1>brother2:
    print("person one is bigger ,and the age is : ",brother1)
else :
    print("person two is bigger ,and the age is :",brother2)
