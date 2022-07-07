"""This is DocString"""

def main():
    """This is DocString"""
    server_a = float(input())
    unit_a = str(input())
    server_b = float(input())
    unit_b = str(input())
    if unit_a == "Millisecond":
        server_a = server_a / 1000
    if unit_b == "Millisecond":
        server_b = server_b / 1000
    if unit_a == "Microsecond":
        server_a = server_a / 1000000
    if unit_b == "Microsecond":
        server_b = server_b / 1000000
    if unit_a == "Nanosecond":
        server_a = server_a / 1000000000
    if unit_b == "Nanosecond":
        server_b = server_b / 1000000000
    if unit_a == "Picosecond":
        server_a = server_a / 1000000000000
    if unit_b == "Picosecond":
        server_b = server_b / 1000000000000
    if server_a < server_b:
        print("Server A, " + str('%.6f' %server_a) + " second")
        print("Faster than server B , " + str(int(server_b // server_a)) + " times")
    elif server_a > server_b:
        print("Server B, " + str('%.6f' %server_b) + " second")
        print("Faster than server A , " + str(int(server_a // server_b)) + " times")
    elif server_a == server_b:
        print("equal")
main()
