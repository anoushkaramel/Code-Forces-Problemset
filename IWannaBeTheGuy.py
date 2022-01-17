p = int(input())
s1 = list(map(int, input("").split()))
s2 = list(map(int, input("").split()))
l = s1[1:]
for i in range(1, s2[0]+1):
    l.append(s2[i])
l.sort()
lev = []
for i in l:
    if(i not in lev):
        lev.append(i)
g=[]
for i in range(1, p+1):
    g.append(i)
if(lev==g):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
