x_1 = 5
for i_1 in range(x_1):
    for i_3 in range(i_1+1):
        print("*",end="")
    for i_2 in range(8-2*(i_1)):
        print(" ",end="")
    for i_4 in range(i_1+1):
        print("*",end="")
    print( )
for j_1 in range(5-x_1):
    for j_3 in range(j_1+1):
        print("*",end="")
    for j_2 in range(8-2*(j_1)):
        print(" ",end="")
    for j_4 in range(j_1+1):
        print("*",end="")
    print( )

y_1 = 5
for j_1 in range(y_1):
    for j_3 in range(4-j_1):
        print("*",end="")
    for j_2 in range(2*(j_1)+2):
        print(" ",end="")
    for j_4 in range(4-j_1):
        print("*",end="")
    print( )