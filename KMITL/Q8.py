"""This is DocString"""

def main():
    """This is DocString"""
    loop = 0
    grop = []
    while loop != 9:
        num = int(input())
        grop.append(num)
        loop += 1
    for roop_1 in range(len(grop)):
        total = 0
        for roop_2 in range(roop_1 + 1, len(grop)):
            test_grop = []
            test_grop = grop.copy()
            det_1 = grop[(len(grop) - 1) - roop_1]
            det_2 = grop[(len(grop) - 1) - roop_2]
            test_grop.remove(det_1)
            test_grop.remove(det_2)
            total = sum(test_grop)
            if total == 100:
                for kuy in test_grop:
                    print(kuy)
                break
        if total == 100:
            break
    if total != 100:
        print("ERROR")
main()
