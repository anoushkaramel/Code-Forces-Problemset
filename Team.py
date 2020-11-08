# Code-Forces-Problemset
Practice problems
n=int(input(''))
l=[]
f=0
while n>0 :
    a,b,c = input('').split()
    a=int(a)
    b=int(b)
    c=int(c)
    l.append(a)
    l.append(b)
    l.append(c)
    t=len(l)
    m=l[t-3:t]
    x=m.count(1)
    if(x>=2):
        f=f+1 
    else:
        f=f+0
    n=n-1
print(f)
