'''
    write a program to figure out shape of object (portrait, landscape, square) using given length and width
'''
lenght = int(input("Enter shape's lenght..."))
width = int(input("Enter shape's width..."))

if lenght==width:
    print("lenth is ",lenght,"width is",width,"given shape is square")
if width>lenght:
    print("lenth is ",lenght,"width is",width,"given shape is landscape")
if width<lenght:
    print("lenth is ",lenght,"width is",width,"given shape is portrait")

print('good bye.')