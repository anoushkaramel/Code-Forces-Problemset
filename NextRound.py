n,k=input('').split()
n=int(n)
k=int(k)
x=[]
l = list(map(int, input().split(' ')[:n]))
for i in l:
    if i>=l[k-1]:
        if i>0:
            x.append(i)
print(len(x))
