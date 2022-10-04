"""Matrix Addition"""

def main():
    """Matrix Addition"""
    matrix = input().split()
    row = int(matrix[0])
    columns = int(matrix[1])
    matrix = []
    for _ in range(row):
        column = input().split()
        matrix.append(list(map(int, column)))
    for val in range(row):
        num = list(map(int, input().split()))
        for add in range(columns):
            matrix[val][add] += num[add]
            print(matrix[val][add], end=" ")
        print("")
main()
