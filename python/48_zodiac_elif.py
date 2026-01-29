'''
    write a program to accept birth day and birth month from user as separate input. decide zodiac sign from below table 
   
    Aquarius: January 20-February 18
    Pisces: February 19-March 20
    Aries: March 21-April 19
    Taurus: April 20-May 20
    Gemini: May 21-June 21
    Cancer: June 22-July 22
    Leo: July 23-August 22
    Virgo: August 23-September 22
    Libra: September 23-October 22
    Scorpio: October 24-November 21
    Sagittarius: November 22-December 21
    Capricorn: December 22-January 19
    '''

date=int(input("enter date of birth of male : "))
month=int(input("enter birth month of male : "))

if month==1 and date>=20 or month==2 and date<=18:
    print("Aquarius")
elif month==2 and date>=19 or month==3 and date<=20:
    print("Pisces")
elif month==3 and date>=21 or month==4 and date<=19:
    print("Aries")
elif month==4 and date>=20 or month==5 and date<=20:
    print("Taurus")
elif month==5 and date>=21 or month==6 and date<=21:
    print("Gemini")
elif month==6 and date>=22 or month==7 and date<=22:
    print("Cancer")
elif month==7 and date>=23 or month==8 and date<=22:
    print("Leo")
elif month==8 and date>=23 or month==9 and date<=22:
    print("Virgo")
elif month==9 and date>=23 or month==10 and date<=22:
    print("Libra")
elif month==10 and date>=24 or month==11 and date<=21:
    print("Scorpio")
elif month==11 and date>=22 or month==12 and date<=21:
    print("Sagittarius")
else:
    print("Capricorn")

date1=int(input("enter date of birth of female : "))
month1=int(input("enter birth month of female : "))

if month1==1 and date1>=20 or month1==2 and date1<=18:
    print("Aquarius")
elif month1==2 and date1>=19 or month1==3 and date1<=20:
    print("Pisces")
elif month1==3 and date1>=21 or month1==4 and date1<=19:
    print("Aries")
elif month1==4 and date1>=20 or month1==5 and date1<=20:
    print("Taurus")
elif month1==5 and date1>=21 or month1==6 and date1<=21:
    print("Gemini")
elif month1==6 and date1>=22 or month1==7 and date1<=22:
    print("Cancer")
elif month1==7 and date1>=23 or month1==8 and date1<=22:
    print("Leo")
elif month1==8 and date1>=23 or month1==9 and date1<=22:
    print("Virgo")
elif month1==9 and date1>=23 or month1==10 and date1<=22:
    print("Libra")
elif month1==10 and date1>=24 or month1==11 and date1<=21:
    print("Scorpio")
elif month1==11 and date1>=22 or month1==12 and date1<=21:
    print("Sagittarius")
else:
    print("Capricorn")

