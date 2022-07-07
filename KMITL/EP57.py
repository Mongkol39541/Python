"""This is DocString"""

def main():
    """This is DocString"""
    total = 0
    stop = 0
    while stop != 10:
        stop += 1
        num = int(input())
        if num < 0:
            num = -5
        total += num
    if total < 0:
        total = -5
    print(total)
main()
