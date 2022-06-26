List = [] 
z = 0
n = int(input("n : "))
for i in range(n):
    x = input("x : ")
    y = input("P(X=x) : ")
    z = x*y
    List.append(z)

print(sum(List))