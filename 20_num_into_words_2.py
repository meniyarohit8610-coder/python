#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 

number=input("enter number of 3 digits...")
number=int(number)

first=number // 10 //10
print(first)

middle=number  // 10 %10 
print(middle)

last=number % 10
print(last)

words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ",words[middle]," ",words[last])