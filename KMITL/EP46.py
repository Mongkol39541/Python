"""This is DocString"""

def function_maf(num, ans):
    """This is DocString"""
    if num > ans:
        ans = num
    elif num <= ans:
        ans = ans
    return ans

def function_mif(num, ans):
    """This is DocString"""
    if num < ans:
        ans = num
    elif num >= ans:
        ans = ans
    return ans

def main():
    """This is DocString"""
    txt = str(input())
    txt = txt.upper()
    num_1 = int(input())
    ans = num_1
    if txt == "MAX":
        ans = function_maf(num_1, ans)
    elif txt == "MIN":
        ans = function_mif(num_1, ans)
    num_2 = int(input())
    if txt == "MAX":
        ans = function_maf(num_2, ans)
    elif txt == "MIN":
        ans = function_mif(num_2, ans)
    num_3 = int(input())
    if txt == "MAX":
        ans = function_maf(num_3, ans)
    elif txt == "MIN":
        ans = function_mif(num_3, ans)
    num_4 = int(input())
    if txt == "MAX":
        ans = function_maf(num_4, ans)
    elif txt == "MIN":
        ans = function_mif(num_4, ans)
    num_5 = int(input())
    if txt == "MAX":
        ans = function_maf(num_5, ans)
    elif txt == "MIN":
        ans = function_mif(num_5, ans)
    if txt == "MAX":
        print("MAX : " + str(ans))
    elif txt == "MIN":
        print("MIN : " + str(ans))
main()
