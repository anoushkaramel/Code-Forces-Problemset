n=int(input(''))
l=list(map(int, input("").split()))
x=0
for i in l:
    if(i==1):
        x=1
        break
if(x):
    print('HARD')
else:
    print("EASY")
