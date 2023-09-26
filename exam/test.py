s = 0
x = [6, 8, 0, 3, 0, 5, 3, 4, 6, 3, 1, 0]
for i in range(1, 13):
    s += (14 - i) * x[i-1] 
print(s)
s = s % 11
if s <= 1:
    print(1 - s)
else:
    print(11 - s)