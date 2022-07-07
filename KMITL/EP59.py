"""This is DocString"""

def main():
    """This is DocString"""
    num_a0 = float(input())
    num_n = float(input())
    num_d = float(input())
    stop = 0
    while stop != num_n:
        stop += 1
        print('%.2f' %num_a0, end=" ")
        num_a0 *= num_d
main()
