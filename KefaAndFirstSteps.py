n=int(input(''))
a = list(map(int, input("").split()))
m=0
l=[]
if(n==1):
    print(1)
else:
    for i in range(n-1):
        if(a[i]<=a[i+1]):
            m=m+1
            if(i==n-2):
                l.append(m)
        else:
            l.append(m)
            m=0
    print(max(l)+1)
