"""Seats Number"""

def main():
    """Seats Number"""
    data = input().upper().replace("[", "").replace("]", "").replace("'", "").split(', ')
    data = [ord(num[0]) * 1000000 + int(num[1:]) for num in data]
    index = int(input())
    cure = 1
    cout = 0
    for _ in range(index):
        hold = data[cure]
        walk = cure - 1
        while walk >= 0 and hold < data[walk]:
            val = data[walk]
            data[walk] = hold
            data[walk + 1] = val
            walk -= 1
            cout += 1
        if walk >= 0:
            cout += 1
        cure += 1
        print([chr(num // 1000000) + str(num % 1000000) for num in data])
    print('Comparison times: {0}'.format(cout))
main()
