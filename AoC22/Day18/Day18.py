# Numpy for easy array stuff
import numpy as np

# Parse the list of cubes into a 3d array
def parse(cubes):
    
    # Find some bounds
    maxX, maxY, maxZ = 0, 0, 0
    cubeCords = []
    
    # For every line
    for c in cubes:
        
        # Split and get values
        c = c.split(',')
        
        cX, cY, cZ = int(c[0]), int(c[1]), int(c[2])
        
        # Find the max
        if cX > maxX:
            maxX = cX
        if cY > maxY:
            maxY = cY
        if cZ > maxZ:
            maxZ = cZ
        
        # Save the parsed coordinates
        cubeCords.append((cX+1, cY+1, cZ+1))
            
    # Create a map that is big enought, plus some padding
    cubeMap = np.zeros((maxX+3, maxY+3, maxZ+3), dtype=bool)
    
    # For every coordinate where there is a cube, set value to true
    for c in cubeCords:
        
        cubeMap[c] = True
    
    # Return the map and the coordinates
    return (cubeMap, cubeCords)

# Function to the the tototal surface area of the cubes
def getSurfaceArea(cubeMap, cubes):
    
    # Init as empty
    area = 0
    
    # For every coordinate
    for c in cubes:
        
        # Check all 6 neighbors. If they are free, add 1
        if c[0] == 0 or not cubeMap[c[0]-1, c[1], c[2]]:
            area += 1
        
        if c[0] == cubeMap.shape[0]-1 or not cubeMap[c[0]+1, c[1], c[2]]:
            area += 1
        
        if c[1] == 0 or not cubeMap[c[0], c[1]-1, c[2]]:
            area += 1
        
        if c[1] == cubeMap.shape[1]-1 or not cubeMap[c[0], c[1]+1, c[2]]:
            area += 1
            
        if c[2] == 0 or not cubeMap[c[0], c[1], c[2]-1]:
            area += 1
        
        if c[2] == cubeMap.shape[2]-1 or not cubeMap[c[0], c[1], c[2]+1]:
            area += 1
    
    # Return the area
    return area
  
# Function to get the outer surface area of the cubes
def getCubesOnSurface(cubeMap):
    
    # Do a BFS. Start from 0,0,0
    start = (0,0,0)
    explored = set()
    frontier = set()
    frontier.add(start)
    
    sides = set()
    
    # While there is anything left to check
    while len(frontier) > 0:
        
        cur = frontier.pop()
        explored.add(cur)
        
        # Check all 6 sides. If it is free, add it to be checked
        # if it is not free, add to the set of surfaces on the outer side
        if cur[0] > 0:
            
            if not cubeMap[cur[0]-1, cur[1], cur[2]]:
                frontier.add((cur[0]-1, cur[1], cur[2]))
            else:
                sides.add(((-1, 0, 0), cur))
    
        if cur[0] < cubeMap.shape[0]-1:
            
            if not cubeMap[cur[0]+1, cur[1], cur[2]]:
                frontier.add((cur[0]+1, cur[1], cur[2]))
            else:
                sides.add(((1, 0, 0), cur))
                
        if cur[1] > 0:
            
            if not cubeMap[cur[0], cur[1]-1, cur[2]]:
                frontier.add((cur[0], cur[1]-1, cur[2]))
            else:
                sides.add(((0, -1, 0), cur))
    
        if cur[1] < cubeMap.shape[1]-1:
            
            if not cubeMap[cur[0], cur[1]+1, cur[2]]:
                frontier.add((cur[0], cur[1]+1, cur[2]))
            else:
                sides.add(((0, 1, 0), cur))
                
        if cur[2] > 0:
            
            if not cubeMap[cur[0], cur[1], cur[2]-1]:
                frontier.add((cur[0], cur[1], cur[2]-1))
            else:
                sides.add(((0, 0, -1), cur))
    
        if cur[2] < cubeMap.shape[2]-1:
            
            if not cubeMap[cur[0], cur[1], cur[2]+1]:
                frontier.add((cur[0], cur[1], cur[2]+1))
            else:
                sides.add(((0, 0, 1), cur))
    
        frontier -= explored

    return len(sides)

# Open input and read as strings
f = open('input.txt', 'r')
cubes = f.read().split('\n')

# Parse the input
cubeMap, cubeCords = parse(cubes)

# Print the results
print(f'The total surface area is {getSurfaceArea(cubeMap, cubeCords)}')
print(f'The outer surface area is {getCubesOnSurface(cubeMap)}')