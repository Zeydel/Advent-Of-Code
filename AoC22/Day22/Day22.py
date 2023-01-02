import numpy as np

def parse(notes):
    
    directions = notes[-1]

    mapNotes = notes[:-2]
    
    maxLength = max([len(l) for l in mapNotes])        
    
    boardMap = np.array([ list(line) + (maxLength - len(line))*[' '] for line in mapNotes ])
    
    return (boardMap, directions)
    
def getStartingPos(boardMap):
    for i, b in enumerate(boardMap[0]):
        if b == '.':
            col = i
            break
        
    return (0, col)
    
def getMappings(boardMap):
    
    mappings = dict()
    
    for i in range(0, boardMap.shape[0], 50):
        for j in range(0, boardMap.shape[1], 50):
            print(i)
            print(j)
            print()

def move(boardMap, pos, steps, turns, curDir):
    for _ in range(steps):
        
        newPos = (pos[0], pos[1])
        
        while True:
        
            pnp = ((newPos[0]+turns[curDir][0]) % boardMap.shape[0], (newPos[1]+turns[curDir][1]) % boardMap.shape[1])
            
            
            if boardMap[pnp] == '.':
                pos = (pnp[0], pnp[1])
                break
            elif boardMap[pnp] == '#':
                break
            elif boardMap[pnp] == ' ':
                newPos = (pnp[0], pnp[1])
                continue
    
    return pos

def moveOnCube(boardMap, pos, steps, turns, curDir):
    for _ in range(steps):
                        
        moveX = turns[curDir][0]
        moveY = turns[curDir][1]
            
        
        potentialPlaces = [(pos[0]+moveX, pos[1]+moveY),
                           (pos[0]+((moveX+moveY)),)]
        
        if boardMap[pos[0]+moveX, pos[1]+moveY] == '.':
            pos = (pos[0]+moveX, pos[1]+moveY)
            continue
        elif boardMap[pos[0]+moveX, pos[1]+moveY] == '#':
            break
        else:
            
            
            
            potentialPlaces = [()]
            
            
            if boardMap[pos[0]+(149*moveX), pos[1]+(149*moveY)] != ' ':
                if boardMap[pos[0]+(149*moveX), pos[1]+(149*moveY)] == '#':
                    break
                else boardMap[pos[0]+(149*moveX), pos[1]+(149*moveY)] == '.':
                    pos = (pos[0]+(149*moveX), pos[1]+(149*moveY))
                    continue
            elif boardMap[pos[0]+((50-(pos[0]%50))*turns[curDir][0]), pos[0]+((50-(pos[0]%50))*turns[curDir+1][1])] != ' ':
                if boardMap[pos[0]+((50-(pos[0]%50))*turns[curDir][0]), pos[0]+((50-(pos[0]%50))*turns[curDir+1][1])] == '#':
                    break
                else
                
            
    return (pos, curDir)
        
# Open input and read as strings
f = open('input.txt', 'r')
notes = f.read().split('\n')

boardMap, directions = parse(notes)

pos = getStartingPos(boardMap)
curDir = 0
turns = [[0,1], [1,0], [0,-1], [-1,0]]

idx = 0

while idx < len(directions):
        
    if directions[idx].isdigit():
        steps = ''
        while idx < len(directions) and directions[idx].isdigit():
            steps += directions[idx]
            idx += 1
            
        pos = move(boardMap, pos, int(steps), turns, curDir)
    else:
        if directions[idx] == 'R':
            curDir += 1
        else:
            curDir -= 1
        
        curDir %= len(turns)
        idx += 1
        
password = (1000 * (pos[0]+1)) + (4 * (pos[1]+1)) + curDir

getMappings(boardMap)

print(password)