"""Min Max"""
def main():
    """Min Max"""
    loop = int(input())
    number = []
    for _ in range(loop):
        num = int(input())
        number.append(num)
    number.sort()
    print(number[0])
    print(number[loop - 1])
main()
