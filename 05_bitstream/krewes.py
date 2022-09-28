import random

'''with open('krewes.txt') as f:
    brr = f.readline()
    '''

hello = "2$$$Yusha$$$dog@@@8$$$craig$$$mommy"
brianchen = {2:[],7:[],8:[]}

def get_devo(krewes):
    person = krewes.split('@@@')
    for i in person:
        mom = i.split('$$$')
        brianchen[int(mom[0])].append([mom[1],mom[2]])
    period = random.choice(list(brianchen.keys()))
    person = random.choice(brianchen[period])
    return(f"{period} : {person[0]},{person[1]}")

print(get_devo(hello))

