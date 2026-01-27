"""
write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements.
"""
num_1=int(input("enter first number : "))
num_2=int(input("enter second number : "))
choice=int(input("enter choise : "))

if choice==1:
    addition=num_1+num_2
    print("addition is : ",addition)
elif choice==2:
    subtraction=num_1-num_2
    print("subtraction is : ",subtraction)
elif choice==3:
    multiplication=num_1*num_2
    print("multiplication is : ",multiplication)
elif choice==4:
    division = num_1 / num_2
    print("divisison is :",division )
else:
    print("enter proper choise !!!!! ")
print(":) :) good byyy :) :) ")