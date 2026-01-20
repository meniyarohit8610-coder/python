'''
write a program to calculate profit or loss amount or no profit no loss & display it using given purchase & sell price.
input: purchase & sale price 
'''
purchase_price = float(input("Enter purchase price... "))
sale_price = float(input("Enter sale price..."))
qty=int(input("enter number of product sale..."))

difference = sale_price - purchase_price
ans=difference*qty

if difference>0:
    print("profit amount is ",ans)

if difference<0:
    print("loss amount is",ans)

if difference==0:
    print("no profit no loss")

print("Good bye.")