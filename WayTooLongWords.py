n=int(input(''))
a=[ ]
while(n>0):
    w=input('')
    a.append(w)
    n=n-1
for i in a:
    l=len(i)
    if (l>10):
        s=i[l-1]
        print(i[0]+str(l-2)+s)
    else:
        print(i)
