a,b,c=input('').split()
a=int(a)
b=int(b)
c=int(c)
s=a*c*(c+1)/2
if(b>s):
    print(0)
else:
    print(int(s-b))
