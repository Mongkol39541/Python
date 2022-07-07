"""This is DocString"""

def calculate(news, yyy, xxx):
    """This is DocString"""
    news = str(input())
    if news != "Stop":
        if news == "North":
            yyy += 2
        elif news == "South":
            yyy -= 2
        elif news == "East":
            xxx += 2
        elif news == "West":
            xxx -= 2
        if yyy > 1:
            yyy = 1
        if yyy < -1:
            yyy = -1
        if xxx > 1:
            xxx = 1
        if xxx < -1:
            xxx = -1
        axis_y, axis_x = calculate(news, yyy, xxx)
    if news == "Stop":
        axis_y = yyy
        axis_x = xxx
    return axis_y, axis_x

def main():
    """This is DocString"""
    dawn = str(input())
    if dawn == "1":
        yyy = 1
        xxx = -1
    elif dawn == "2":
        yyy = 1
        xxx = 1
    elif dawn == "3":
        yyy = -1
        xxx = -1
    elif dawn == "4":
        yyy = -1
        xxx = 1
    axis_y, axis_x = calculate(dawn, yyy, xxx)
    if axis_y == 1 and axis_x == -1:
        print("1")
    elif axis_y == 1 and axis_x == 1:
        print("2")
    elif axis_y == -1 and axis_x == -1:
        print("3")
    elif axis_y == -1 and axis_x == 1:
        print("4")
main()
