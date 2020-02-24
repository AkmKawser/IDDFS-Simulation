locations = {
    'A': ['B', 'C', 'D'],
    'B': ['E','F'],
    'C': ['G'],
    'D': ['H'],
    'E':['I'],
    'F':['J','K'],
    'G':['L'],
    'H':['M','N'],
    'I':[None],
    'J':[None],
    'K':['O','P'],
    'L':['R'],
    'M':[None],
    'N':['S'],
    'O':[None],
    'P':[None],
    'R':[None],
    'S':[None]
}


def DLS(source,depth):
    start=locations[source]
    print(source, end=' ')
    if start[0] is None:
        return
    if depth==0:
        return
    else:
        for location in start:
            listt = location
            for place in listt:
                DLS(place,depth-1)

def iddfs(source,max_height):
    for i in range(max_height+1):
        print('depth: '+str(i)+': ',end=' ')
        DLS(source,i)
        print()

iddfs('A',4)