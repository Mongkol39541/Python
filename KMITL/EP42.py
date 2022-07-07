"""This is DocString"""

def calculate(cal):
    """This is DocString"""
    if cal == 1:
        ans = " ^----^"
    elif cal == 2:
        ans = "( 0--0 )"
    elif cal == 3:
        ans = "<------>"
    elif cal == 4:
        ans = "(------)"
    elif cal == 5:
        ans = " u----u"
    return ans

def main():
    """This is DocString"""
    ans_1 = calculate(int(input()))
    ans_2 = calculate(int(input()))
    ans_3 = calculate(int(input()))
    ans_4 = calculate(int(input()))
    ans_5 = calculate(int(input()))
    print(ans_1)
    print(ans_2)
    print(ans_3)
    print(ans_4)
    print(ans_5)
main()
