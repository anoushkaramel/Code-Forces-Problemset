s=input('')
s=s.lower()
m=''
a=[]
v=['a','e','i','o','u','y']
l=list(s)
for i in l:
    if i not in v:
        a.append(i)
for i in a:
    m=m+'.'+i 
print(m)
