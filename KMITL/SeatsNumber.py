"""Seats Number"""

def main():
    """Seats Number"""
    data = input().upper().replace("[", "").replace("]", "").replace("'", "").split(', ')
    data = [ord(num[0]) * 1000000 + int(num[1:]) for num in data]
    index = int(input())
    cure = 0
    cout = 0
    for _ in range(index):
        samll = cure
        walk = cure + 1
        while walk <= index:
            if data[walk] < data[samll]:
                samll = walk
            walk += 1
            cout += 1
        val = data[cure]
        data[cure] = data[samll]
        data[samll] = val
        cure += 1
        print([chr(num // 1000000) + str(num % 1000000) for num in data])
    print('Comparison times: {0}'.format(cout))
main()
