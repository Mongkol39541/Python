"""This is DocString"""

def funtionchange(axis_int2d, table_2d):
    """This is DocString"""
    for row in range(len(table_2d)):
        for column in range(len(table_2d[row])):
            for num in axis_int2d:
                if row == num[0] and column == num[1]:
                    table_2d[row][column] = "*"
    return table_2d

def calculate(axis_int2d, table_2d):
    """This is DocString"""
    for row in range(len(table_2d)):
        for column in range(len(table_2d[row])):
            for num in axis_int2d:
                if row == num[0] and column == num[1]:
                    if row != 0:
                        val_n = table_2d[row - 1][column]
                        table_2d[row - 1][column] = val_n + 1
                        if column != 0:
                            val_n = table_2d[row - 1][column - 1]
                            table_2d[row - 1][column - 1] = val_n + 1
                        if column != (len(table_2d) - 1):
                            val_n = table_2d[row - 1][column + 1]
                            table_2d[row - 1][column + 1] = val_n + 1
                    if row != (len(table_2d) - 1):
                        val_s = table_2d[row + 1][column]
                        table_2d[row + 1][column] = val_s + 1
                        if column != 0:
                            val_s = table_2d[row + 1][column - 1]
                            table_2d[row + 1][column - 1] = val_s + 1
                        if column != (len(table_2d) - 1):
                            val_s = table_2d[row + 1][column + 1]
                            table_2d[row + 1][column + 1] = val_s + 1
                    if column != 0:
                        val_e = table_2d[row][column - 1]
                        table_2d[row][column - 1] = val_e + 1
                    if column != (len(table_2d) - 1):
                        val_w = table_2d[row][column + 1]
                        table_2d[row][column + 1] = val_w + 1
    return table_2d

def funtiontable(mxn_int):
    """This is DocString"""
    table_2d = []
    for _ in range(mxn_int[0]):
        table = []
        for _ in range(mxn_int[1]):
            table.append(0)
        table_2d.append(table)
    return table_2d

def main():
    """This is DocString"""
    mxn = str(input())
    mxn = mxn.lower()
    mxn = mxn.split('x')
    boom = int(input())
    axis_2d = []
    mxn_int = []
    axis_int2d = []
    for _ in range(boom):
        axis = str(input())
        axis = axis.split(',')
        axis_2d.append(axis)
    kuy = axis_2d.copy()
    total = 0
    for row in kuy:
        total += 1
        for column in range(total, boom):
            if row == kuy[column]:
                axis_2d.remove(row)
                break
    for num in mxn:
        num = int(num)
        mxn_int.append(num)
    for axis_1d in axis_2d:
        axis_int = []
        for num in axis_1d:
            num = int(num)
            axis_int.append(num)
        axis_int2d.append(axis_int)
    table_2d = funtiontable(mxn_int)
    table_2d = calculate(axis_int2d, table_2d)
    table_2d = funtionchange(axis_int2d, table_2d)
    row = 0
    column = 0
    for row in range(len(table_2d)):
        for column in range(len(table_2d[row])):
            print(table_2d[row][column], end=" ")
        print("")
main()
