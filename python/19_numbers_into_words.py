#write a program to convert given 2 digit amount into words


ammount = input("Enter number (2 digit)...") 
ammount = int(ammount)
last = ammount % 10 #3
# print(last)
first = ammount // 10 #5
# print(first)
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ",words[last])