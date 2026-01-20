''' 
        1) write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
        input : 15 hours 
        output  3 PM 

        input : 11 hours 
        output  11 AM 

        input : 25 hours 
        output  invalid input 
'''

hour=int(input("enter houres in form of 24(hour)..."))

import sys

if hour>24:
     print("invalid choise , choose number between 1 to 24 only !!!!!!")
     sys.exit()

if hour<=12:
    print("time is ",hour,"am")
if hour>12:
     print("time is ",hour-12,"pm")


print("good byy.")