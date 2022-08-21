"""[Onsite Day 2] Atbash Cipher"""

def cal1(txt, txt_1, txt_2):
    """DDD"""
    for mes in range(len(txt_1)):
        if txt == txt_1[mes]:
            txt = txt_2[mes]
            break
    return txt

def main():
    """DDD"""
    total = str(input())
    small_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", \
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    small_2 = small_1.copy()
    small_2.sort(reverse=True)
    big_1 = []
    for kuy in small_1:
        big_1.append(kuy.upper())
    big_2 = big_1.copy()
    big_2.sort(reverse=True)
    ans = []
    for txt in total:
        txt = cal1(txt, small_1, small_2)
        txt = cal1(txt, big_1, big_2)
        ans.append(txt)
    for num in range(len(ans)):
        print(ans[num], end="")
main()
