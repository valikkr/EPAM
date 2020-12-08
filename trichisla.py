a = int(input())
b = int(input())
c = int(input())
x= (a>=b) and (a>=c)
y= (b>=a) and (b>=c)
z= (c>=a) and (c>=b)
if x == True :
    if b >=c:
        print (a)
        print (c)
        print (b)
    else :
        print (a)
        print (b)
        print (c)
elif y == True :
    if a >=c:
        print (b)
        print (c)
        print (a)
    else :
        print (b)
        print (a)
        print (c)
elif z == True :
    if b >=a:
        print (c)
        print (a)
        print (b)
    else :
        print (c)
        print (b)
        print (a)
