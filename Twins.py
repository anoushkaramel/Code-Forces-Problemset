n=int(input(''))
l=list(map(int, input("").split()))
s=0
x=0
y=0
for i in l:
    s=s+i
for i in range(n-1):
    for j in range(n-i-1):
        if(l[j]>l[j+1]):
            a=l[j]
            l[j]=l[j+1]
            l[j+1]=a
while(s>=x):
    x=x+l[n-1]
    s=s-l[n-1]
    y=y+1
    n=n-1
print(y)
