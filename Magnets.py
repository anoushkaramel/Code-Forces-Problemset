n=int(input(''))
l=[]
g=0
if(n==1):
    print(1)
else:
    for i in range(n):
        p=int(input(''))
        l.append(p)
    for i in range(n-1):
        if(l[i]!=l[i+1]):
            g=g+1
    print(g+1)
