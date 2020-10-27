n,k=input('').split()
m=int(n)
l=int(k)
while l>0:
    if(m%10==0):
        m=m//10
    else:
        m=m-1
    l=l-1
print(m)
