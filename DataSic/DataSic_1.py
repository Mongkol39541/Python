y = 1
x = 20
i = 0
for j in range(20):
    for z in range(x):
        print(" " ,end="")
    x = x-1
    for l in range(y):
        print("*",end="")
    y = y+2
    i = i+1
    if i == 6 :
        i = 0
        x = x+2
        y = y-4
    print( )
o = 15
p = 10
for e in range(p):
    for f in range(o):
        print(" " ,end="")
    for s in range(p):
        print("*",end="")
    print( )