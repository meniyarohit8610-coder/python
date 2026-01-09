##write a program to convert given 3 digit amount into words
# input : 175 output : one hundred seventy five  

number=input("enter number of 3 digits...")
number=int(number)

first=number // 10 //10
print(first)

middle=number  // 10 %10 
print(middle)

last=number % 10
print(last)

words=['zero','hundred','two_hundread','three_hunded','four_hundread','five_hundread','six_hundread','seven_hundread','eight_hundread','nine_hundread']
words2=['zero','ten','twenty','therty','fourty','fifty','sixty','seventy','eighty','ninety']
words3 = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first]," ",words2[middle]," ",words3[last])
