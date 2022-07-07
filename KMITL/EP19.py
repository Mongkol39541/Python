"""This is DocString"""

def main():
    """This is DocString"""
    num = float(input())
    stin = str(input())
    num_up = ((num + 4) ** (1 / 4)) + (num / 4)
    num_down = (4 * num) - 4
    num_ans = (num_up / num_down) * 44
    num_final = num // 44
    print(stin * int(num_final))
    print('%.4f' %num_ans)
main()
