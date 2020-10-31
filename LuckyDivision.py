n=int(input(''))
l=[4,7,44,47,74,77,444,447,474,477,74,747,774,777]
for i in l:
    if(n==i or n%i==0):
        c = True
        break
    else:
        c = False
if(c == True):
    print('YES')
else:
    print('NO')
