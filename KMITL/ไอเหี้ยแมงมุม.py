"""[Onsite Day 2] เกมวิ่งเก็บ"""

def calculate_0(num, che):
    """DDD"""
    print("* " * ((num * 2) - che), end="")
    che += 4
    return che

def calculate_1(num, tum):
    """DDD"""
    print("  " * (num - tum), end="")
    print("* ", end="")
    print("  " * (num - tum), end="")
    tum += 2
    return tum

def calculate_up(num, room, boom, che, tum):
    """DDD"""
    for loop in range(num -1):
        if loop % 2 == 0:
            for _ in range(room):
                print("  ", end="")
                print("* ", end="")
            che = calculate_0(num, che)
            for _ in range(room):
                print("* ", end="")
                print("  ", end="")
            room += 1
        if loop % 2 == 1:
            kuy = 1
            for iii in range(boom):
                if iii == boom - 1:
                    kuy = 2
                print("  ", end="")
                print("* " * kuy, end="")
            tum = calculate_1(num, tum)
            for iii in range(boom):
                if iii != 0:
                    kuy = 1
                print("* " * kuy, end="")
                print("  ", end="")
            boom += 1
        print("")
    return num, room, boom, che, tum

def calculate_low(num, room, boom, che, tum):
    """DDD"""
    for loop in range(num -1):
        if loop % 2 == 0:
            che -= 4
            for _ in range(room):
                print("  ", end="")
                print("* ", end="")
            che = calculate_0(num, che)
            for _ in range(room):
                print("* ", end="")
                print("  ", end="")
            room -= 1
            che -= 4
        if loop % 2 == 1:
            tum -= 2
            kuy = 1
            for iii in range(boom):
                if iii == boom - 1:
                    kuy = 2
                print("  ", end="")
                print("* " * kuy, end="")
            tum = calculate_1(num, tum)
            for iii in range(boom):
                if iii != 0:
                    kuy = 1
                print("* " * kuy, end="")
                print("  ", end="")
            boom -= 1
            tum -= 2
        print("")
    return num, room, boom, che, tum

def main():
    """DDD"""
    num = int(input())
    print("* " + "  " * (num - 1) + "* " + "  " * (num - 1) + "* ")
    room = 1
    boom = 1
    che = 3
    tum = 3
    num, room, boom, che, tum = calculate_up(num, room, boom, che, tum)
    print("* " * ((num * 2) + 1))
    room -= 1
    boom -= 1
    num, room, boom, che, tum = calculate_low(num, room, boom, che, tum)
    print("* " + "  " * (num - 1) + "* " + "  " * (num - 1) + "* ")
main()
