import random as r

with open('krewes.txt') as f:
    krewes = f.readline()

classes = {2:[],7:[],8:[]}

def get_devo(krewes):
    #split list into person
    person = krewes.split('@@@')

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

