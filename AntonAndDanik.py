n=int(input(''))
s=input('')
a=0
d=0
for i in s:
    if(i=='A'):
        a=a+1
    if(i=='D'):
        d=d+1
if(a>d):
    print('Anton')
elif(a<d):
    print('Danik')
else:
    print('Friendship')
