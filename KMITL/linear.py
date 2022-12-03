
def cost(x, y, z, che=False):
    value = (1500 * x) + (2000 * y) + (1000 * z)
    if value <= 60000:
        che = True
    return value, che

def hour(x, y, z, che=False):
    value = (5 * x) + (7 * y) + (4 * z)
    if value <= 52:
        che = True
    return value, che

def area(x, y, z, che=False):
    value = x + y + z
    if value <= 15:
        che = True
    return value, che

profit = 0
for x in range(105):
    for y in range(75):
        for z in range(14):
            x = x / 10
            y = y / 10
            value_cost, che_cost = cost(x, y, z)
            value_hour, che_hour = hour(x, y, z)
            value_area, che_area = area(x, y, z)
            if che_cost and che_hour and che_area:
                presen = (1200 * x) + (1500 * y) + (800 * z)
                if profit <= presen:
                    ans_x = x
                    ans_y = y
                    ans_z = z
                    profit = presen
print("ตอบในรูปทศนิยม")
print("x =", ans_x)
print("y =", ans_y)
print("z =", ans_z)
print("กำไรสูงสุ =", profit)

print("")

profit = 0
for x in range(11):
    for y in range(8):
        for z in range(14):
            value_cost, che_cost = cost(x, y, z)
            value_hour, che_hour = hour(x, y, z)
            value_area, che_area = area(x, y, z)
            if che_cost and che_hour and che_area:
                presen = (1200 * x) + (1500 * y) + (800 * z)
                if profit <= presen:
                    ans_x = x
                    ans_y = y
                    ans_z = z
                    profit = presen
print("ตอบในรูปจำนวนเต็ม")
print("x =", ans_x)
print("y =", ans_y)
print("z =", ans_z)
print("กำไรสูงสุ =", profit)