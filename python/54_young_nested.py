#write a program to findout most young person from 4 person given age

person_1=int(input("enter first person age...."))
person_2=int(input("enter second person age...."))
person_3=int(input("enter third person age...."))
person_4=int(input("enter four person age...."))

if person_1==person_2==person_3==person_4:
    print("all have same age!!!")
else:
    if person_1<person_2 and person_1<person_3 and person_1<person_4:
        print("person 1 is young!!!")
    elif person_2<person_1 and person_2<person_3 and person_2<person_4:
        print("person 2 is young!!!")
    elif person_3<person_1 and person_3<person_2 and person_3<person_4:
        print("person 3 is young!!!")
    else:
        print("person 4 is young !!!")
    