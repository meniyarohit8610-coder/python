iphone17_ind=float(input("enter price in india..."))
iphone17_usa=float(input("enter price in usa ..."))

ans=iphone17_usa*38.5/100
total=iphone17_usa+ans

if iphone17_ind<total:
    print("purchase from india is better than usa :) :) ",iphone17_ind)

else:
    print("purchase from usa is better than india  :) :) ",total)