''' assume % add to 100'''

import random as r

'''with open('occupations.py') as f:
    stbdict = f.readlines()'''

stbdict = [["WOOFWOOF","50.6"],["GRR","24.4"],["Yusha","14.5"],["VScOde","10.5"]]

def randomizer(lst):
    pdict = {}
    for i in lst:
        pdict[i[0]] = int(float(i[1])*10)
    num = r.randrange(0,1000)
    upper = 0
    lower = 0
    for i in list(pdict.keys()):
        upper += pdict[i]
        if lower <= num and num < upper:
            return i
        lower += pdict[i]

def testes():
    numdict = {}
    for i in stbdict:
        numdict[i[0]] = 0
    for i in range(10000):
        k = randomizer(stbdict)
        numdict[k] += 1
    for i in stbdict:
        print(f"{i[0]} \n\tintended: {i[1]} \n\tactual: {float(int(numdict[i[0]])/100)}")

testes()
        

