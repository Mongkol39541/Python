"""This is DocString"""

def dolist(num):
    """This is DocString"""
    keep = []
    for che in range(num):
        keep.append(che + 1)
    return keep

def main():
    """This is DocString"""
    num = int(input())
    keep = dolist(num)
    name_1 = 0
    roop = 0
    while len(keep) != 1:
        name_2 = name_1 + 1
        if name_2 >= len(keep):
            name_2 -= name_1 + 1
        print("Round {0} : Person {1} killed \
person {2}".format(roop + 1, keep[name_1], keep[name_2]))
        del keep[name_2]
        name_1 += 1
        if name_1 >= len(keep):
            name_1 = 0
        roop += 1
    print("Person {0} is the winner".format(keep[0]))
main()
