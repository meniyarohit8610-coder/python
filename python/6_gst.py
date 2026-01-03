'''
wap to calculate gst tax ammount from given bill ammount and tax rate 
'''
ammount=0
rate=0

ammount=input("enter ammount of bill..")
rate=input("enter tare of tax (%)..")

ammount=float(ammount)
rate=float(rate)

tax=ammount*rate/100

print("ammount after all gst and taxt is ...",tax)