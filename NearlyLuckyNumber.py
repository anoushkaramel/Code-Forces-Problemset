n=int(input(''))
x=0
for i in str(n):
    if(i=='4' or i=='7'):
        x=x+1
if(x==4 or x==7):
    print('YES')
else:
    print('NO')
