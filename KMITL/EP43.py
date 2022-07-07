"""This is DocString"""

def function_f(num):
    """This is DocString"""
    num = (15 + num - num **3) / (((num ** 2) / 3) + 11)
    return num

def function_g(num):
    """This is DocString"""
    num = (num ** 3) + (4 * num) - 1
    return num

def main():
    """This is DocString"""
    num = float(input())
    txt = str(input())
    txt = txt.lower()
    if txt == "fog":
        num = function_g(num)
        num = function_f(num)
    elif txt == "gof":
        num = function_f(num)
        num = function_g(num)
    print('%.2f' %num)
main()
