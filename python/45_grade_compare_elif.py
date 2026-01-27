'''Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90-100     | A+    |
| 80-89      | A     |
| 70-79      | B     |
| 60-69      | C     |
| 50-59      | D     |
| below 50   | Need to improve  |
----------------------------------------
'''
sub1=int(input("enter subject one marks   : "))
sub2=int(input("enter subject two marks   : "))
sub3=int(input("enter subject three marks : "))
sub4=int(input("enter subject four marks  : "))
sub5=int(input("enter subject five marks  : "))

total=sub1+sub2+sub3+sub4+sub5
per=total/5

print("total of all subject is :",total)
print("percentage is :",per)

if per<50:
    print("you need to improve !!!!")
elif per>=50 and per<59:
    print("grade : D")
elif per>=60 and per<69:
    print("grade : C")
elif per>=70 and per<79:
    print("grade : B")
elif per>=80 and per<89:
    print("grade : A")
else :
    print("grade : A+")


