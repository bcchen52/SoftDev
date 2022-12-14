
from flask import Flask
app = Flask(__name__) #create instance of class Flask

import random as r

with open('occupations.csv') as f:
    stbdict = f.readlines()

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
        strlst += (f"{splitlst[i][0]}<br>") #create a string with every occupation
    return(f"{header}<br>{strlst}<br><br>{randomizer()[0]}")

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
