"""This is DocString"""

import math

def main():
    """This is DocString"""
    num_x = float(input())
    num_y = float(input())
    disp = float(input())
    degr = float(input())
    cos_x = (math.cos(degr * (math.pi / 180)) * disp) + num_x
    sin_y = (math.sin(degr * (math.pi / 180)) * disp) + num_y
    dist_x = round(cos_x, 2)
    dist_y = round(sin_y, 2)
    print('%.2f' %dist_x)
    print('%.2f' %dist_y)
main()
