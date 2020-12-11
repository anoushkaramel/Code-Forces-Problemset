s=input('')
t=''
if(len(s)==1):
    if(s.isupper()):
        print(s.lower())
    else:
        print(s.upper())
else:
    if((s[0].islower() and s[1:].isupper()) or s.isupper()):
        for i in s:
            if(i.isupper()):
                i=i.lower()
                t=t+i
            else:
                i=i.upper()
                t=t+i
        print(t)
    else:
        print(s)
