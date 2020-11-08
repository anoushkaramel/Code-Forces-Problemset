s=input('')
a=list(s)
u=0
l=0
for i in a:
    if(i.isupper()):
        u=u+1
    else:
        l=l+1
if(u>l):
    print(s.upper())
elif(u<=l):
    print(s.lower())
