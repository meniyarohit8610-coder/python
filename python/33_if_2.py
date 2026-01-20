'''
    write a program to figure out shape of object (portrait, landscape, square) using given length and width
'''
length = int(input("Enter shape's length..."))
width = int(input("Enter shape's width..."))

if length==width:
    print("lenth is ",length,"width is",width,"given shape is square")
if width>length:
    print("lenth is ",length,"width is",width,"given shape is landscape")
if width<length:
    print("lenth is ",length,"width is",width,"given shape is portrait")

print('good bye.')