#write a program to figure out whether given number  is perfect number or not
import sys
number=int(input("enter the number : "))

while number:
    if 2*number*number-1 /2 :
        print('number is perfect number ...')
        sys.exit()
    if 2*number*number /2 :
        print('number is not perfect number ...')
print('good by')