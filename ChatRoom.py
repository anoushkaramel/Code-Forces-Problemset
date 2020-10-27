s=input('')
h='hello'
a=0
for i in range (len(s)):
    if(s[i]==h[a]):
        a=a+1
    if(a==5):
            break
if(a==5):
    print('YES')
else:
    print('NO')
