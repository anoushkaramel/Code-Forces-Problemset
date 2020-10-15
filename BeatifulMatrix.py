l1 = list(map(int, input("").split()))
l2 = list(map(int, input("").split()))
l3 = list(map(int, input("").split()))
l4 = list(map(int, input("").split()))
l5 = list(map(int, input("").split()))
if (1 in l1):
    x=1
    y=l1.index(1)+1
elif (1 in l2):
    x=2
    y=l2.index(1)+1
elif (1 in l3):
    x=3
    y=l3.index(1)+1
elif (1 in l4):
    x=4
    y=l4.index(1)+1
else:
    x=5
    y=l5.index(1)+1
print(abs(3-x) + abs(3-y))
