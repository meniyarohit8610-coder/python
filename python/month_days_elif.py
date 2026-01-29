'''
    write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days 
    '''
    
days=int(input("enter number to print how many days : "))
import sys
if days==2:
    print("28")
    sys.exit()
elif days==1 or  days==3 or days==5 or days==7 or days==8 or days== 10 or days==12 :
    print("this month have 31 days !!!")
    sys.exit()
elif days==4 or days==6 or days==9 or days==11 :
    print("this month have 30 days !!!")
    sys.exit()
else :
    print("enter valid choice !!!")