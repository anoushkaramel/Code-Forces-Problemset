n,t=input('').split()
n=int(n)
t=int(t)
s=input('')
m=''
l=list(s)
while(t>0):
    i=0
    while(i<n-1):
        if(l[i]=='B' and l[i+1]=='G'):
            c=l[i]
            l[i]=l[i+1]
            l[i+1]=c
            i=i+2
        else:
            i=i+1
    t=t-1
for j in l:
    m=m+j
print(m)
