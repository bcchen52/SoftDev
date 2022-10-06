
from flask import Flask
app = Flask(__name__) #create instance of class Flask

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


def randomizer():
    num = r.randrange(0,int(total*10))
    upper = 0
    lower = 0
    for i in list(pdict.keys()):
        upper += pdict[i]
        if lower <= num and num < upper:
            return (f"Occupation: {i}",i)
        lower += pdict[i]

@app.route("/")#this is the root route
def display():
    header = "Brian, Andrew, Yusha<br>SoftDev<br>K08 -- Serve<br>2022-10-06<br>"
    strlst = ""
    for i in range(0,len(splitlst)):
        strlst += (f"{splitlst[i][0]}, ")
    return(f"{header}<br>{strlst}<br><br>{randomizer()[0]}")

@app.route("/testes/<sx>")
def testes(sx): #plural for test, runs randomizer and gives %
    x = int(sx)
    final = ""
    totalerror = 0.0
    numdict = {}
    for i in splitlst:
        numdict[i[0]] = 0
    for i in range(x):
        k = randomizer()[1]
        numdict[k] += 1
    for i in splitlst:
        actual = float(int(numdict[i[0]])/(x/100))
        final += f"{i[0]} <br>     intended: {i[1]} <br>     actual: {round(actual,2)}<br>"
        error = abs(actual-float(i[1]))/float(i[1]) #percent error equation
        totalerror += error
    return(f"{final}<br>Average error is {round((100*totalerror)/len(splitlst),2)}%")

print(testes(100))


@app.route("/test")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "sdh"


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
