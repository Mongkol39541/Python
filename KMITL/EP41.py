"""This is DocString"""

def calculate(cal, num, hour, txt):
    """This is DocString"""
    ans = (cal * 30 * num * hour) / 1000
    ans = '%.2f' %ans
    return str(txt) + " " + str(cal) + " Watt " + str(num) + " ea f" + "or \
" + str(hour) + " hours\n" + str(ans) + " unit."

def main():
    """This is DocString"""
    ans_1 = calculate(int(input()), 1, 3, "TV")
    ans_2 = calculate(int(input()), 1, 1, "Microwave")
    ans_3 = calculate(int(input()), 1, 0.5, "Hair dryer")
    ans_4 = calculate(int(input()), 4, 5, "light bulb")
    ans_5 = calculate(int(input()), 1, 24, "Refrigerator")
    print(ans_1)
    print(ans_2)
    print(ans_3)
    print(ans_4)
    print(ans_5)
main()
