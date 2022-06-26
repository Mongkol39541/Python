import numpy as np
List = ["x_1","x_2","x_3","x_4","x_5","x_6","x_7","x_8","x_9"," x_10"] 
Table = []
Table_1 = []

for i_1 in range(10):
  for i_2 in range(10):
    List[i_2] = i_2*10 + i_1
    Table.append(List[i_2])
  Table_1.append(Table)
  Table = []

Data = np.array([Table_1[0],Table_1[9],Table_1[2],Table_1[7],Table_1[4],Table_1[5],Table_1[6],Table_1[3],Table_1[8],Table_1[1]])

Data_2 = []
Data_3 = []

for j_1 in range(10):
  for j_2 in range(10):
    Data_1 = Data[j_2][j_1]
    Data_2.append(Data_1)
  Data_3.append(Data_2)
  Data_2 = []
Ans = np.array(Data_3)

print(Ans)