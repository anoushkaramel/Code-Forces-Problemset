s=input('')
l=[1,2,3]
t=''
m=[]
x=[]
for i in s:
    if(i!='+'):
        m.append(i)
m.sort()
for j in m:
    t=t+j+'+'
j=len(t)
print(t[0:(j-1)])
