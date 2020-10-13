n=int(input(''))
x=0
while (n>0):
    i=input('')
    if (i=='X++' or i=='++X'):
        x=x+1
    else:
        x=x-1
    n=n-1
print(x)
