n=int(input(''))
a=list(map(int, input('').split()))
a=sorted(a)
s=''
for i in a:
    s=s+str(i)+' '
print(s)
