"""This is DocString"""

def dolist(num):
    """This is DocString"""
    keep = []
    for che in num:
        keep.append(che)
    return keep

def main():
    """This is DocString"""
    num_1 = str(input())
    num_2 = str(input())
    keep_1 = dolist(num_1)
    keep_2 = dolist(num_2)
    total = 0
    for roop_1 in range(len(num_1)):
        ans = abs(int(keep_1[roop_1]) - int(keep_2[roop_1]))
        if ans > 5:
            ans = 10 - ans
        total += ans
    print(total)
main()
