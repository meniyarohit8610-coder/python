#write a program to figure out whether given number  is armstrong number or not
num=int(input("Enter a number to check armstrong or not : "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")
    