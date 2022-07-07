"""This is DocString"""

def function_miff(ans, num):
    """This is DocString"""
    if num < ans:
        ans_1 = num
        ans_2 = ans
    elif num >= ans:
        ans_1 = ans
        ans_2 = num
    return ans_1, ans_2

def function_mif(ans, num):
    """This is DocString"""
    if num < ans:
        ans_3 = num
    elif num >= ans:
        ans_3 = ans
    return ans_3

def main():
    """This is DocString"""
    num_01 = int(input())
    num_02 = int(input())
    ans_01, ans_02 = function_miff(num_01, num_02)
    ans_3 = ans_02
    stop = 0
    while stop != 8:
        stop += 1
        num = int(input())
        ans_1, ans_2 = function_miff(ans_01, num)
        if ans_2 != ans_1:
            ans_3 = function_mif(ans_2, ans_02)
        if ans_3 == ans_1:
            ans_3 = ans_2
        ans_01 = ans_1
        ans_02 = ans_3
    print("Almost the min : " + str(ans_02))
main()
