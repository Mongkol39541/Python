"""Pythagorus"""

def main():
    """Pythagorus"""
    num = input().split()
    val_1 = float(num[0])
    val_2 = float(num[1])
    val_3 = (val_1**2 + val_2**2) ** (1/2)
    print('%.6f' %val_3)
main()
