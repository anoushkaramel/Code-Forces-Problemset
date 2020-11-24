n=int(input(''))
l=list(map(int, input("").split()))
s=''
for i in range (1,n+1):
    s=s+str(l.index(i)+1)+' '
print(s)
