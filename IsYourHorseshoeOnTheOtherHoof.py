s = list(map(int, input("").split()))
uniq = []
for i in s:
    if(i not in uniq):
        uniq.append(i)
hs = 0
for i in uniq:
    a = s.count(i)
    hs = hs + a - 1
print(hs)
