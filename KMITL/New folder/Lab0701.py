"""Insertion Sort"""
 
def main():
    """Insertion Sort"""
    data = input()
    data = data[1:len(data) - 1]
    data = data.split(', ')
    data = [int(num) for num in data]
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
        print(data)
    print('Comparison times: {0}'.format(cout))
main()