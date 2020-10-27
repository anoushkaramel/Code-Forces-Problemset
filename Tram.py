n=int(input(''))
f=n
m=[]
x=[]
p=0
while (n>0):
    a,b=input('').split()
    a=int(a)
    b=int(b)
    m.append(a)
    m.append(b)
    n=n-1
for i in range (0,f):
    p=p-m[(2*i)]
    p=p+m[((2*i)+1)]
    x.append(p)
print(max(x))
