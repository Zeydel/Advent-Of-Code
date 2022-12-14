# Everything is easier in numpy
import numpy as np

# Parse the input into a np array 
def parse(rocks):
    
    # Start by finding the bounds of x and y
    minX, maxX = float('inf'), float('-inf')
    minY, maxY = 0, float('-inf')
    for l in rocks:
        for r in l.split(' -> '):
            
            x, y = int(r.split(',')[0]), int(r.split(',')[1])
            
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            if y < minY:
                minY = y
            if y > maxY:
                maxY = y
    
    # Create an array that size and fill with boid
    rockMap = np.chararray(((maxX+1)-minX, (maxY+1)-minY))
    rockMap[:] = '.'
    
    # Go through every pair of rock lines
    for l in rocks:
        pairs = l.split(' -> ')
        
        # Fill the spaces with rocks
        for i,p in enumerate(pairs[:-1]):
            
            sX, sY = int(pairs[i].split(',')[0]), int(pairs[i].split(',')[1])
            eX, eY = int(pairs[i+1].split(',')[0]), int(pairs[i+1].split(',')[1])
            
            sX, eX = min(sX, eX), max(sX, eX)
            sY, eY = min(sY, eY), max(sY, eY)
            
            rockMap[sX-minX:eX+1-minX,sY-minY:eY+1-minY] = '#'
        
    # Return the map and the minimum X
    return rockMap, minX

# Function to spawn some sand
def createSand(rockMap, minX):
    
    # Spawn at the spawn point
    sp = (500-minX, 0)
    
    while True:
    
        # If we are at the bottom edge, return the map unaltered
        if sp[1] >= rockMap.shape[1]-1:
            return rockMap
        
        # Go down if possible
        if rockMap[sp[0], sp[1]+1] == b'.':
            sp = (sp[0], sp[1]+1)
            continue
            
        # If we cant go down and we are at the left edge, return the map unaltered
        if sp[0] <= 0:
            return rockMap
        
        # Go down and left if possible
        if rockMap[sp[0]-1, sp[1]+1] == b'.':
            sp = (sp[0]-1, sp[1]+1)
            continue
            
        # If we cant go left or down and we are at the right edge, return map
        if sp[0] >= rockMap.shape[0]:
            return rockMap
        
        # Else go down and right if possible
        if rockMap[sp[0]+1, sp[1]+1] == b'.':
            sp = (sp[0]+1, sp[1]+1)
            continue
        
        # If we cant move anything, settle the sand and return the map
        rockMap[sp] = b'o'
        return rockMap
    

# Altered version of the above function.
def createSandFloor(rockMap, minX):
    
    sp = (500-minX, 0)
    
    while True:
        
        # Settle the sand on the bottom
        if sp[1] >= rockMap.shape[1]-1:
            rockMap[sp] = b'o'
            return (rockMap, minX)
        
        if rockMap[sp[0], sp[1]+1] == b'.':
            sp = (sp[0], sp[1]+1)
            continue
          
        # If we are on the left edge, pad the map with a column, adjust positional vars
        if sp[0] <= 0:
            rockMap = np.r_[[np.array([b'.']*rockMap.shape[1])], rockMap]
            minX -= 1
            sp = (sp[0]+1, sp[1])
            continue
        
        if rockMap[sp[0]-1, sp[1]+1] == b'.':
            sp = (sp[0]-1, sp[1]+1)
            continue
            
        # If we are on the right edge, pad the map with a column
        if sp[0] >= rockMap.shape[0]-1:
            rockMap = np.r_[rockMap, [np.array([b'.']*rockMap.shape[1])]]
            continue
        
        if rockMap[sp[0]+1, sp[1]+1] == b'.':
            sp = (sp[0]+1, sp[1]+1)
            continue
        
        rockMap[sp] = b'o'
        return (rockMap, minX)
    

# Open input and read as strings
f = open('input.txt', 'r')
rocks = f.read().split('\n')

# Parse the input and init the result var
rockMap, minX = parse(rocks)
rounds = 0

# While true
while(True):
    
    # Save a copy of the old map
    old = np.copy(rockMap)
    
    # Generate the new map
    rockMap = createSand(rockMap, minX)
    
    # If nothing changed, break 
    if (rockMap == old).all():
        break

    # Increment rounds
    rounds += 1
   
# Reset the map and add an empty row on the bottom
rockMap, minX = parse(rocks)
rockMap = np.c_[rockMap, np.array([b'.']*rockMap.shape[0])]

# Init the result var
roundsToBlock = 0

# While the spawner is free
while rockMap[500-minX, 0] != b'o':

    # Create sand
    rockMap, minX = createSandFloor(rockMap, minX)
    roundsToBlock += 1
   
# Print the results
print(f'It takes {rounds} rounds for the sand to fall into the void')
print(f'It takes {roundsToBlock} before the spawner is blocked')