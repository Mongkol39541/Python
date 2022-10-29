# Find-S Algorithm
# 27/10/2022

# Copyright (C) 2022

def expand(X, S):
    for i in range(len(S)):
        if X[i] != S[i] and S[i] == '':
            S[i] = X[i]
        elif X[i] != S[i] and S[i] != '':
            S[i] = '?'
    return S

def FindS(X, T):
    S = [''] * len(X[0])
    for i in range(len(X)):
        if T[i] == 'Yes':
            S = expand(X[i], S)
    return S

if __name__ == '__main__':
    X = [['Sunny', 'Warm', 'Normal', 'Strong', 'Cool', 'Change'],
    ['Cloudy', 'Warm', 'Normal', 'Strong', 'Cool', 'Change'],
    ['Rainy', 'Warm', 'Normal', 'Strong', 'Cool', 'Change']]
    T = ['Yes', 'Yes', 'No']
    S = FindS(X, T)
    print(S)

# เนื่องจากได้สมมติฐานที่จำเพาะที่สุดเพียงสมมติฐานเดียว อาจทำให้บางกรณีที่สอดคล้องกับตัวอย่างลบ
# แก้โดยสร้างสมมติฐานลบขึ้นมา