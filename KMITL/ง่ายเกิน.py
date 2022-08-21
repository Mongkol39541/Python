"""[Onsite Day 2] เกมวิ่งเก็บ"""

def main():
    """DDD"""
    txt = input()
    pog = txt.split()
    total = []
    for num in pog:
        total.append(float(num))
    ans = 0
    lcm = 0
    for kuy in range(len(total)):
        ans += abs(lcm - total[kuy])
        lcm = total[kuy]
    print('%.2f'%ans)
main()
