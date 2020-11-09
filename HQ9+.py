s=input('')
b=0
for i in s:
    if(i=='H' or i=='Q' or i=='9'):
        b=True
if(b):
    print('YES')
else:
    print('NO')
