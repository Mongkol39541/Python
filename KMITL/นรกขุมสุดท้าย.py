"""This is DocString"""

def slip(total_num, group_txt, mes):
    """This is DocString"""
    count = 0
    kuy = 0
    ans = []
    for txt in mes:
        num = 0
        if count == 3:
            kuy += 1
            count = 0
            if kuy == 3:
                kuy = 0
        for time in range(len(group_txt)):
            if txt == group_txt[time].lower():
                num = time
                num -= total_num[kuy]
                ans.append(group_txt[num])
                break
        if txt == " ":
            ans.append(" ")
            count -= 1
        count += 1
    return ans

def pair(txt, group_txt):
    """This is DocString"""
    num = 0
    for read in txt:
        for time in range(len(group_txt)):
            if read == group_txt[time].lower():
                num += time
                if num >= 26:
                    num -= 26
                elif num < -26:
                    num += 26
                break
    return num

def main():
    """This is DocString"""
    mes = str(input())
    mes = mes.lower()
    txt_1 = str(input())
    txt_1 = txt_1.lower()
    txt_2 = str(input())
    txt_2 = txt_2.lower()
    txt_3 = str(input())
    txt_3 = txt_3.lower()
    num = 0
    group_txt = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', \
    'Y', 'Z']
    total_txt = [txt_1, txt_2, txt_3]
    total_num = []
    for txt in total_txt:
        num = pair(txt, group_txt)
        total_num.append(num)
    ans = slip(total_num, group_txt, mes)
    boss = ""
    for out in ans:
        boss += out
    boss = boss.capitalize()
    print(boss)
main()
