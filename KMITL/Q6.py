"""This is DocString"""

def main():
    """This is DocString"""
    num = int(input())
    kuy = 4
    total = 1
    for roop in range(num // 2):
        if roop == 0:
            print("* " * num)
        else:
            print("* ", end="")
            print("  " * (total - 1), end="")
            print("* ", end="")
            print("  " * (num - kuy), end="")
            print("* ", end="")
            print("  " * (total - 1), end="")
            print("* ")
            kuy += 2
            total += 1
    if num % 2 != 0:
        print("* ", end="")
        print("  " * (total - 1), end="")
        print("* ", end="")
        print("  " * (total - 1), end="")
        print("* ")
        kuy = 1
    else:
        kuy = 0
    for lcm in range(num // 2, 0, -1):
        if lcm == 1:
            print("* " * num)
        else:
            print("* ", end="")
            print("  " * (lcm - 2), end="")
            print("* ", end="")
            print("  " * kuy, end="")
            print("* ", end="")
            print("  " * (lcm - 2), end="")
            print("* ")
            kuy += 2
main()
