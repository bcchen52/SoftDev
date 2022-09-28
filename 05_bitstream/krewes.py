import random as r

with open('krewes.txt') as f:
    krewes = f.readline()

classes = {2:[],7:[],8:[]}

def get_devo(krewes):
    person = krewes.split('@@@')
    for i in person:
        pinfo = i.split('$$$')
        classes[int(pinfo[0])].append([pinfo[1],pinfo[2]])
    pd = r.choice(list(classes.keys()))
    person = r.choice(classes[pd])
    return(f"{pd} : {person[0]}, ducky named: {person[1]}")

print(get_devo(krewes))

