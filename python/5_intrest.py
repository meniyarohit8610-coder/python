'''
simple intrest 
'''
p=0
r=0
n=0

p=input("enter principal (ammount): ")
r=input("enter rate of interest : ")
n=input("enter number of year : ")

p=float(p)
r=float(r)
n=float(n)

ans=p*r*n/100

print("interest is ",ans)
