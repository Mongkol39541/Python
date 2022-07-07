"""This is DocString"""

def calculate_1(axis_a, axis_b, axis_c):
    """This is DocString"""
    if axis_a == 1:
        print("A")
    elif axis_b == 1:
        print("B")
    elif axis_c == 1:
        print("C")

def calculate_2(axis_a, axis_b, axis_c):
    """This is DocString"""
    if axis_a == 2:
        print("A")
    elif axis_b == 2:
        print("B")
    elif axis_c == 2:
        print("C")

def calculate_3(axis_a, axis_b, axis_c):
    """This is DocString"""
    if axis_a == 3:
        print("A")
    elif axis_b == 3:
        print("B")
    elif axis_c == 3:
        print("C")

def calculate_12(axis_a, axis_b, axis_c):
    """This is DocString"""
    if axis_a == 1 and axis_b == 2:
        axis_a += 1
        axis_b -= 1
    elif axis_a == 1 and axis_c == 2:
        axis_a += 1
        axis_c -= 1
    elif axis_a == 2 and axis_b == 1:
        axis_a -= 1
        axis_b += 1
    elif axis_a == 2 and axis_c == 1:
        axis_a -= 1
        axis_c += 1
    elif axis_b == 1 and axis_c == 2:
        axis_b += 1
        axis_c -= 1
    elif axis_b == 2 and axis_c == 1:
        axis_b -= 1
        axis_c += 1
    return axis_a, axis_b, axis_c

def calculate_23(axis_a, axis_b, axis_c):
    """This is DocString"""
    if axis_a == 2 and axis_b == 3:
        axis_a += 1
        axis_b -= 1
    elif axis_a == 2 and axis_c == 3:
        axis_a += 1
        axis_c -= 1
    elif axis_a == 3 and axis_b == 2:
        axis_a -= 1
        axis_b += 1
    elif axis_a == 3 and axis_c == 2:
        axis_a -= 1
        axis_c += 1
    elif axis_b == 2 and axis_c == 3:
        axis_b += 1
        axis_c -= 1
    elif axis_b == 3 and axis_c == 2:
        axis_b -= 1
        axis_c += 1
    return axis_a, axis_b, axis_c

def calculate_13(axis_a, axis_b, axis_c):
    """This is DocString"""
    if axis_a == 1 and axis_b == 3:
        axis_a += 2
        axis_b -= 2
    elif axis_a == 1 and axis_c == 3:
        axis_a += 2
        axis_c -= 2
    elif axis_a == 3 and axis_b == 1:
        axis_a -= 2
        axis_b += 2
    elif axis_a == 3 and axis_c == 1:
        axis_a -= 2
        axis_c += 2
    elif axis_b == 1 and axis_c == 3:
        axis_b += 2
        axis_c -= 2
    elif axis_b == 3 and axis_c == 1:
        axis_b -= 2
        axis_c += 2
    return axis_a, axis_b, axis_c

def main():
    """This is DocString"""
    num_n = int(input())
    stop = 0
    axis_a = 1
    axis_b = 2
    axis_c = 3
    while stop != num_n:
        num_abc = str(input())
        if num_abc == "12" or num_abc == "21":
            axis_a, axis_b, axis_c = calculate_12(axis_a, axis_b, axis_c)
        elif num_abc == "23" or num_abc == "32":
            axis_a, axis_b, axis_c = calculate_23(axis_a, axis_b, axis_c)
        elif num_abc == "13" or num_abc == "31":
            axis_a, axis_b, axis_c = calculate_13(axis_a, axis_b, axis_c)
        stop += 1
    calculate_1(axis_a, axis_b, axis_c)
    calculate_2(axis_a, axis_b, axis_c)
    calculate_3(axis_a, axis_b, axis_c)
main()
