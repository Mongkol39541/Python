"""This is DocString"""

def row_3(time, txt, num):
    """This is DocString"""
    if time % 3 != 0:
        if time == 1:
            print("♦.{0}.♦".format(txt), end="")
        elif (time - 1) % 3 == 0:
            print(".{0}.♦".format(txt), end="")
        elif time == num:
            print(".{0}.♦".format(txt), end="")
        elif (time + 1) % 3 == 0:
            print(".{0}.".format(txt), end="")
    elif time % 3 == 0:
        print("◊.{0}.◊".format(txt), end="")

def row_2(time, num):
    """This is DocString"""
    if time % 3 != 0:
        if time == 1:
            print(".♦.♦.", end="")
        elif (time - 1) % 3 == 0:
            print("♦.♦.", end="")
        elif time == num:
            print("♦.♦.", end="")
        elif (time + 1) % 3 == 0:
            print("♦.♦", end="")
    elif time % 3 == 0:
        print(".◊.◊.", end="")

def row_1(time, num):
    """This is DocString"""
    if time % 3 != 0:
        if time == 1:
            print("..♦..", end="")
        elif (time - 1) % 3 == 0:
            print(".♦..", end="")
        elif time == num:
            print(".♦..", end="")
        elif (time + 1) % 3 == 0:
            print(".♦.", end="")
    elif time % 3 == 0:
        print("..◊..", end="")

def main():
    """This is DocString"""
    txt = str(input())
    num = len(txt)
    time = 0
    while time != num:
        time += 1
        row_1(time, num)
    print("")
    time = 0
    while time != num:
        time += 1
        row_2(time, num)
    print("")
    time = 0
    while time != num:
        time += 1
        row_3(time, txt[time - 1], num)
    print("")
    time = 0
    while time != num:
        time += 1
        row_2(time, num)
    print("")
    time = 0
    while time != num:
        time += 1
        row_1(time, num)
    print("")
main()
