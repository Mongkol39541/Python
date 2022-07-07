"""This is DocString"""

def main():
    """This is DocString"""
    num_a0 = int(input())
    num_n = int(input())
    num_d = int(input())
    stop = 0
    while stop != num_n:
        stop += 1
        print(num_a0, end=" ")
        num_a0 += num_d
main()
