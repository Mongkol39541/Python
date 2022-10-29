import numpy as np

def expand(X, S):
    for i in range(len(S)):
        if X[i] != S[i] and S[i] == '':
            S[i] = X[i]
        elif X[i] != S[i] and S[i] != '':
            S[i] = '?'
    return S

def negexpand(X, S, G, fal):
    for j in fal:
        for i in range(len(S)):
            if S[i] != X[j][i] and S[i] != '?':
                g = ['?'] * len(X[j])
                g[i] = S[i]
                if g[i] not in G:
                    G.append(g)
    return G

def sumexpand(S, G, SG):
    for g in G:
        for i in range(len(S)):
            if S[i] != g[i] and S[i] != '?':
                f = g.copy()
                f[i] = S[i]
                if f not in SG:
                    SG.append(f)
    return SG

def FindS(X, T):
    S = [''] * len(X[0])
    G = []
    SG = []
    fal = []
    for i in range(len(X)):
        if T[i] == 'Yes':
            S = expand(X[i], S)
        elif T[i] == 'No':
            fal.append(i)
    G = negexpand(X, S, G, fal)
    SG = sumexpand(S, G, SG)
    return SG

if __name__ == '__main__':
    X = [['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'Hight', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'Hight', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'Hight', 'Strong', 'Cool', 'Change']]
    T = ['Yes', 'Yes', 'No', 'Yes']
    SG = FindS(X, T)
    print(SG)