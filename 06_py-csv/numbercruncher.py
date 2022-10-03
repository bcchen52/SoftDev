'''
Brian Chen 
Soft Dev
K06 -- py-csv
2022-09-30
time spent: 60 mins

DISCO:
If an entry has a , in it, it is enclosed with "" instead of '' (I think)
You can use this to show the law of large numbers

QCC:


'''

import random as r

with open('occupations.csv') as f:
    stbdict = f.readlines()

#stbdict = [["WOOFWOOF","50.6"],["GRR","24.4"],["Yusha","14.5"],["VScOde","10.5"]]

splitlst = [] 

stbdict.pop(0) #remove header

for i in stbdict: #splice list
    i = i[:-1]
    if '''"''' in i:
        i = i[1:] #if the occupation in "", remove first "
        splitlst.append(i.split('",'))          
    else:
        i.split(',')
        splitlst.append(i.split(','))

total = float(splitlst.pop(-1)[1]) #remove last entry, total. Number used to calculate percent

pdict = {}

for i in splitlst:
    pdict[i[0]] = int(float(i[1])*10)

def randomizer(lst):
    num = r.randrange(0,int(total*10))
    upper = 0
    lower = 0
    for i in list(pdict.keys()):
        upper += pdict[i]
        if lower <= num and num < upper:
            return i
        lower += pdict[i]


def testes(x): #plural for test, runs randomizer and gives %
    totalerror = 0
    numdict = {}
    for i in splitlst:
        numdict[i[0]] = 0
    for i in range(x):
        k = randomizer(splitlst)
        numdict[k] += 1
    for i in splitlst:
        actual = float(int(numdict[i[0]])/(x/100))
        print(f"{i[0]} \n\tintended: {i[1]} \n\tactual: {round(actual,2)}")
        error = abs(actual-float(i[1]))/float(i[1]) #percent error equation
        totalerror += error
    return(f"Average error is {round((100*totalerror)/len(splitlst),2)}%")

print(testes(1000000))
        

