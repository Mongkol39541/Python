"""This is DocString"""

def main():
    """This is DocString"""
    num_1 = int(input())
    num_2 = int(input())
    total = 0
    print("Integer Pass : ", end="")
    if num_1 % 2 != 0:
        total += num_1
        print(str(num_1) + " ", end="")
    while num_1 < num_2:
        if num_1 % 2 != 0:
            num_1 = num_1 + 2
            if num_1 <= num_2:
                total += num_1
                print(str(num_1) + " ", end="")
        else:
            num_1 = num_1 + 1
            if num_1 <= num_2:
                total += num_1
                print(str(num_1) + " ", end="")
    while num_1 > num_2:
        if num_1 % 2 != 0:
            num_1 = num_1 - 2
            if num_1 >= num_2:
                total += num_1
                print(str(num_1) + " ", end="")
        else:
            num_1 = num_1 - 1
            if num_1 >= num_2:
                total += num_1
                print(str(num_1) + " ", end="")
    print("")
    print("Sum Answer : " + str(total))
main()
