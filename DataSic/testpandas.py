import pandas as pd

Row = ["A","B","C","D","E","F","G"]
Column = [1,2,3,4,5,6,7]
Data = []
Teble_2 = []

for i_1 in range(7):
    for i_2 in range(7):
        Teble_1 = str(Row[i_1])+str(Column[i_2])
        Teble_2.append(Teble_1)
    Data.append(Teble_2)
    Teble_2 = []

s = pd.Series(Data)
print(s)