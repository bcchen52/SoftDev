'''
Brian Chen 
Soft Dev
K05 -- bistream
2022-09-29
time spent: 30 mins

DISCO:
When you split a String, the String entry has a backslash n at the back. We manually remove it from the last entry with [:-1]. If not, there will be an extra line when you return.
Use open('filename') as f to open a text file, and f.readline() to read a txt file with one line of text. 
You can assign random to a variable, in this case r.

QCC:
...
'''


import random as r

with open('krewes.txt') as f:
    krewes = f.readline()

classes = {2:[],7:[],8:[]}

def get_devo(krewes):
    #split list into person
    person = krewes.split('@@@')
    person[-1] = person[-1][:-1]

    for i in person:
        #split each person's information into [pd,name,ducky]
        pinfo = i.split('$$$')

        #classes[pd].append([name,ducky])
        classes[int(pinfo[0])].append([pinfo[1],pinfo[2]])

    #pick pd from .keys()
    pd = r.choice(list(classes.keys()))

    person = r.choice(classes[pd])
    return(f"{pd} : {person[0]}, ducky named: {person[1]}")

print(get_devo(krewes))

