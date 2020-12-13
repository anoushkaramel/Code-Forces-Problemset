a=input('')
b=input('')
t=''
l=len(a)
for i in range(l):
    if(a[i]==b[i]):
        t=t+'0'
    else:
        t=t+'1'
print(t)
