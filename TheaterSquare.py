# Code-Forces-Problemset
Practice problems
a,b,c = input('').split()
a=int(a)
b=int(b)
c=int(c)
l=a//c
m=a%c
x=b//c
y=b%c
if(m==0):
    u=l
else:
    u=l+1 
if(y==0):
    v=x
else:
    v=x+1
print(u*v)
