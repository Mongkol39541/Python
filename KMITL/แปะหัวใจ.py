"""[Onsite Day 2] เกมวิ่งเก็บ"""

def degflip(txt_group):
    """DDD"""
    for txt in range(len(txt_group)):
        for num in range(len(txt_group[0]) - 1, -1, -1):
            print(txt_group[txt][num], end="")
        print("")

def deg180(txt_group):
    """DDD"""
    for txt in range(len(txt_group) - 1, -1, -1):
        for num in range(len(txt_group[0]) - 1, -1, -1):
            print(txt_group[txt][num], end="")
        print("")

def deg90(txt_group):
    """DDD"""
    for txt in range(len(txt_group[0])):
        for num in range(len(txt_group) - 1, -1, -1):
            print(txt_group[num][txt], end="")
        print("")

def main():
    """DDD"""
    deg = input()
    loop = int(input())
    txt_group = []
    che = True
    for _ in range(loop):
        txt = input()
        txt_group.append(txt)
    for num in range(1, len(txt_group)):
        if len(txt_group[0]) != len(txt_group[num]):
            che = False
    if deg == "90" and che:
        deg90(txt_group)
    elif deg == "180" and che:
        deg180(txt_group)
    elif deg == "flip" and che:
        degflip(txt_group)
    else:
        print("Invalid size")
main()
