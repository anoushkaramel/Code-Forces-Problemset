n=int(input(''))
l=[]
m=x=y=0
while n>0:
    a,b,c = input('').split()
    a=int(a)
    b=int(b)
    c=int(c)
    l.append(a)
    l.append(b)
    l.append(c)
    n=n-1
for i in l[0::3]:
    m=m+i
for j in l[1::3]:
    x=x+j
for k in l[2::3]:
    y=y+k
if(m==0 and x==0 and y==0):
    print('YES')
else:
    print('NO')
