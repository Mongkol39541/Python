"""This is DocString"""

def main():
    """This is DocString"""
    num_a1 = int(input())
    num_a2 = int(input())
    num_a3 = int(input())
    num_a4 = int(input())
    num_c1 = int(input())
    num_c2 = int(input())
    num_c3 = int(input())
    num_c4 = int(input())
    num_b1 = num_c1 - num_a1
    num_b2 = num_c2 - num_a2
    num_b3 = num_c3 - num_a3
    num_b4 = num_c4 - num_a4
    det_a = (num_a1 * num_a4) - (num_a2 * num_a3)
    det_b = (num_b1 * num_b4) - (num_b2 * num_b3)
    det_c = (num_c1 * num_c4) - (num_c2 * num_c3)
    print("b1: " +  str(num_b1))
    print("b2: " +  str(num_b2))
    print("b3: " +  str(num_b3))
    print("b4: " +  str(num_b4))
    print("D: " + str('%.2f' %(det_a + det_b + det_c)))
main()
