"""SelectionSort"""

def main():
    """SelectionSort"""
    data = input()
    data = data[1:len(data) - 1]
    data = data.split(', ')
    data = [int(num) for num in data]
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
        print(data)
    print('Comparison times: {0}'.format(cout))
main()
