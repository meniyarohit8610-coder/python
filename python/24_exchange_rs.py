'''
write a program to display dinominations of currency for given amount
input : 887 Rupees 
output : 
500 x 1 = 500
200 x 1 = 200
100 x 1 = 100
50 x 1 =  50
20 x 1 =  20
10 x 1 =  10
5 x 1 =   05
2 x 1 =   02
1 x 1 =   01
'''
amount = int(input("Enter the amount: "))

r2000=amount // 2000
amount % 2000

r500=amount // 500
amount %= 500

r200=amount // 200
amount %= 200

r100=amount // 100
amount %= 100

r50=amount // 50
amount %= 50

r20=amount // 20
amount %= 20

r10=amount // 10
amount %= 10

r5=amount // 5
amount %= 5

r2=amount // 2
amount %= 2

r1=amount

print("2000 :", r2000)
print("500  :", r500)
print("200  :", r200)
print("100  :", r100)
print("50   :", r50)
print("20   :", r20)
print("10   :", r10)
print("5    :", r5)
print("2    :", r2)
print("1    :", r1)