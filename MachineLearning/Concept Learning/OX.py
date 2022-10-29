# Tic-Tac-Toe
#27/10/2022
# Copyright (C) 2022

import numpy as np
import random

ooo = []
xxx = []
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def checkWin(P):
    for w in win:
        if all(x-1 in P for x in w):
            return True
    return False

def displayOX():
    ox = np.array([''] * 9)
    ox[ooo] = ['O']
    ox[xxx] = ['X']
    print(ox.reshape([3, 3]))

def AI():
    validmove = list(set(range(9)) - set(ooo + xxx))
    V = [-100] * 9
    for m in validmove:
        tempX = xxx + [m]
        V[m], criticalmove = evalOX(ooo, tempX)
        if len(criticalmove) > 0:
            move = [i - 1 for i in criticalmove if i-1 in validmove]
            return random.choice(move)
    
    maxV = max(V)
    imaxV = [i for i, j in enumerate(V) if j == maxV]
    return random.choice(imaxV)

def evalOX(ooo, xxx):
    SO, SX, criticalmove = calSOX(ooo, xxx)
    return 1 + SX - SO, criticalmove

def calSOX(ooo, xxx):
    SO = SX = 0
    criticalmove = []
    for w in win:
        o = [i-1 in ooo for i in w]
        x = [i-1 in xxx for i in w]
        if not any(x):
            nO = o.count(True)
            SO += nO
            if nO == 2:
                print('critical', w)
                criticalmove = w
        if not any(o):
            SX += x.count(True)
    return SO, SX, criticalmove

while True:
    move = int(input('Choose position [1-9]')) - 1
    while move in ooo + xxx or move > 8 or move < 0:
        move = int(input('Bad move : Choose position [1-9]')) - 1
    ooo.append(move)
    displayOX()
    if checkWin(ooo):
        print('O win')
        break
    if len(ooo) + len(xxx) == 9:
        print('Draw')
        break
    xxx.append(AI())
    displayOX()
    if checkWin(xxx):
        print('X win')
        break
    if len(ooo) + len(xxx) == 9:
        print('Draw')
        break