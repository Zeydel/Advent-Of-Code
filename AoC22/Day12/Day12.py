# Easy arrays
import numpy as np

# Get the height of a character. Just ASCII value unless its a S or E
def getHeight(character):
    if character == 'S':
        return ord('a')
    elif character == 'E':
        return ord('z')
    else:
        return ord(character)

# Find the next positions that we can go to given a placement and the map
def getNextPosisitions(current, heightMap):
    
    x, y = current[0]
    curHeight = getHeight(heightMap[x,y])
    
    newNodes = []
    
    # Check that we are inside bounds and we dont go too far up
    if x > 0 and getHeight(heightMap[x-1, y]) <= curHeight + 1:
        newNodes.append(((x-1, y), current[1]+1))

    if x < heightMap.shape[0]-1 and getHeight(heightMap[x+1, y]) <= curHeight + 1:
        newNodes.append(((x+1, y), current[1]+1))

    if y > 0 and getHeight(heightMap[x, y-1]) <= curHeight + 1:
        newNodes.append(((x, y-1), current[1]+1))

    if y < heightMap.shape[1]-1 and getHeight(heightMap[x, y+1]) <= curHeight + 1:
        newNodes.append(((x, y+1), current[1]+1))

    return newNodes

def getNextPositionDownhill(current, heightMap):
    
    x, y = current[0]
    curHeight = getHeight(heightMap[x,y])
    
    newNodes = []
    
    # Check that we are inside bounds and we dont go too far down
    if x > 0 and getHeight(heightMap[x-1, y]) >= curHeight - 1:
        newNodes.append(((x-1, y), current[1]+1))

    if x < heightMap.shape[0]-1 and getHeight(heightMap[x+1, y]) >= curHeight - 1:
        newNodes.append(((x+1, y), current[1]+1))

    if y > 0 and getHeight(heightMap[x, y-1]) >= curHeight - 1:
        newNodes.append(((x, y-1), current[1]+1))

    if y < heightMap.shape[1]-1 and getHeight(heightMap[x, y+1]) >= curHeight - 1:
        newNodes.append(((x, y+1), current[1]+1))

    return newNodes
    
# Open input and read as strings
f = open('input.txt', 'r')
heightMap = f.read().split('\n')

# Turn the input into a np array
heightMap = np.asarray([np.asarray([j for j in i]) for i in heightMap])

# Find the S
SPos = np.where(heightMap == 'S')[0][0], np.where(heightMap == 'S')[1][0]

# Init the BFS vars
unexplored = []
unexplored.append((SPos, 0))

explored = set()
explored.add((SPos))

distFromS = -1

# Do a BFS
while len(unexplored) > 0:
    
    current = unexplored.pop(0)
    if heightMap[current[0]] == 'E':
        distFromS = current[1]
        break
    
    for npos in getNextPosisitions(current, heightMap):
        if npos[0] not in explored:
            unexplored.append(npos)
            explored.add(npos[0])

# Find all the a's
aPosX = np.where(heightMap == 'a')[0]
aPosY = np.where(heightMap == 'a')[1]


# Perform a BFS from the end to an a
EPos = np.where(heightMap == 'E')[0][0], np.where(heightMap == 'E')[1][0]

unexplored = []
unexplored.append((EPos, 0))

explored = set()
explored.add(EPos)

distFromA = float('inf')

while len(unexplored) > 0:
        
    current = unexplored.pop(0)
                
    if heightMap[current[0]] == 'a':
        bestDistFromA = current[1]
        break
        
    for npos in getNextPositionDownhill(current, heightMap):
        if npos[0] not in explored:
            unexplored.append(npos)
            explored.add(npos[0])
    
# Print the results
print(f'The quickest path from S to E is {distFromS} steps')
print(f'The quickest path from a to E is {bestDistFromA} steps')