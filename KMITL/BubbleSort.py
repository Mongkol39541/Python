"""BubbleSort"""

def main():
    """BubbleSort"""
    data = input()
    data = data[1:len(data) - 1]
    data = data.split(', ')
    data = [int(num) for num in data]
    index = int(input())
    cure = 0
    sor = False
    cout = 0
    while cure <= index and sor == False:
        walk = index
        sor = True
        while walk > cure:
            if data[walk] < data[walk - 1]:
                sor = False
                val = data[walk]
                data[walk] = data[walk - 1]
                data[walk - 1] = val
            walk -= 1
            cout += 1
        cure += 1
        print(data)
    print('Comparison times: {0}'.format(cout))
main()
