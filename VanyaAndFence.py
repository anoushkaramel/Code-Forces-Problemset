n,h=input('').split()
n=int(n)
h=int(h)
l=list(map(int, input("").split()))
r=0
for i in l:
    if(i>h):
        r=r+2
    else:
        r=r+1
print(r)
