a,b = input('').split()
a=int(a)
b=int(b)
c=1
while c>0:
    a=3*a
    b=2*b
    if(a>b):
        print(c)
        break
    else:
        c=c+1
