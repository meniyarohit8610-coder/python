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
ammount=int(input("enter total ammount ... "))

rs500=ammount // 500
ammount %= 500

rs200=ammount//200
ammount %= 200

rs100=ammount//100
ammount %= 100

rs50=ammount//50
ammount %= 50

rs20=ammount//20
ammount %= 20

rs10=ammount//10
ammount %= 10

rs5=ammount//5
ammount %= 5

rs2=ammount//2
ammount %= 2

rs1=ammount

print("rupees 500 notes is ",rs500)
print("rupees 200 notes is ",rs200)
print("rupees 100 notes is ",rs100)
print("rupees 50 notes is ",rs50)
print("rupees 20 notes is ",rs20)
print("rupees 10 notes is ",rs10)
print("rupees 5 notes is ",rs5)
print("rupees 2 notes is ",rs2)
print("rupees 1 notes is ",rs1)


