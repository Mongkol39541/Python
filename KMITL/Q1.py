"""This is DocString"""

def main():
    """This is DocString"""
    num_1 = int(input())
    num_2 = int(input())
    ans = (num_1 * num_2) // 100
    lcm = num_2 - ans
    print("(" + ("O" * ans) + ("_" * lcm) + ") " + str(num_1) + "%")
main()
