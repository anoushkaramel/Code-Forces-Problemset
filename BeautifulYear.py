n=int(input(''))
a=n+1
while(a>n):
    m=[]
    for i in str(a):
        if(i not in m):
            m.append(i)
    if(len(m)==4):
        break
    else:
        a=a+1
print(a)
