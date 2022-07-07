"""This is DocString"""

def main():
    """This is DocString"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    numx = int(input())
    numy = int(input())
    ans_up = (numb / ((numa ** 2) / numd) + numx * (numb / numa)) * numy
    ans_down = numy * numc
    ans_ture = ans_up / ans_down
    print('%.2f' %ans_ture)
main()
