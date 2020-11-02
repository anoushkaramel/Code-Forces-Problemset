n=int(input(''))
s=0
if(n<=5):
    print(1)
elif(n%5 == 0):
    print(n//5)
else:
    print(n//5 + 1)
