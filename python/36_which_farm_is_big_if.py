#write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 

length=float(input("enter total length of farm1 ..."))
width=float(input("enter total width of farm 1 ..."))

total=length*width

print("**********************************************************")

length2=float(input("enter total length of farm2 ..."))
width2=float(input("enter total width of farm 2 ..."))

total2=length2*width2

print(total)
print(total2)

if total>total2:
    print("total size is ",total2,"farm 1 is gratter!!!")
if total<total2:
    print("total size is ",total,"farm 2 is gratter!!!")
if total==total2:
    print("both farms are sam ")

print(":) :) thank you :) :)")