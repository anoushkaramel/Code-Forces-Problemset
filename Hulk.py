n=int(input(""))
s='I hate'
if(n==1):
    print('I hate it')
else:
    for i in range(2,n+1):
        if(i%2==0):
            s=s+' that I love'
        else:
            s=s+' that I hate'
    print(s+ ' it')
