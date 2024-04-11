"""Seats Number"""
 
def main():
    """Seats Number"""
    data = input().upper().replace("[", "").replace("]", "").replace("'", "").split(', ')
    data = [ord(num[0]) * 1000000 + int(num[1:]) for num in data]
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
        print([chr(num // 1000000) + str(num % 1000000) for num in data])
    print('Comparison times: {0}'.format(cout))
main()