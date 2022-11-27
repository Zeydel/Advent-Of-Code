# I need my tools
import re
from itertools import permutations
import numpy as np

# Parse the list of diagnostics into a list of nodes
def parse(diagnostics):
    
    # Empty list
    nodes = []
    
    # Ignore the headers, but take every other line
    for d in diagnostics[2:]:
        
        # Split to parse
        s = d.split()
        
        # Get all the values
        x = int(re.findall(r'x(\d+)', s[0])[0])
        y = int(re.findall(r'y(\d+)', s[0])[0])
        
        size = int(s[1][:-1])
        used = int(s[2][:-1])
        avail = int(s[3][:-1])
        use = int(s[4][:-1])
        
        # Add the node to the list
        nodes.append([x, y, size, used, avail, use])
        
    # Return the list
    return nodes
        
# Parse the list of nodes into a grid
def makeGrid(nodes):
    
    # Find the bounds
    maxX = max(n[0] for n in nodes)
    maxY = max(n[1] for n in nodes)
    
    # Create a chararray of the given size
    grid = np.chararray((maxY+1, maxX+1))
    
    # For every node
    for n in nodes:
        
        # If the size is too big, it is usless
        if n[3] > 150:
            grid[n[1],n[0]] = '#'
        # If it is empty, mark it
        elif n[3] == 0:
            grid[n[1],n[0]] = '_'
        # Else it is just a normal node
        else:
            grid[n[1],n[0]] = '.'
    
    # Mark the data we need
    grid[0, maxX] = 'G'
    
    # Return the grid
    return grid

# Check if a pair is viable
def isViable(A, B):
    
    # Not viable if A is empty
    if A[5] == 0:
        return False
    
    # Not viable if A doesn't fit in B
    if A[3] > B[4]:
        return False
    
    # Else it is true
    return True

# Count all the viable pairs
def getViablePairs(nodes):
    
    # Counter
    pairCount = 0
    
    # Get all pairs
    for c in permutations(nodes, 2):
        
        # Count the viable ones
        if isViable(c[0], c[1]):
            pairCount += 1
            
    return pairCount
        
# Move the data one step left and count how many steps it takes
def moveOneLeft(grid):
    
    # Find the data
    Gpos = np.where(grid == b'G')
    Gcord = list(zip(Gpos[0], Gpos[1]))[0]
    
    # Find the empty node
    Epos = np.where(grid == b'_')
    Ecord = list(zip(Epos[0], Epos[1]))[0]
    
    # Find the spot one left of the data
    goal = (Gcord[0], Gcord[1]-1)
    
    # Do a BFS to find out how many steps to take the empty node to
    # the left of the data
    unexplored = [(Ecord, 0)]
    explored = set()
    
    while len(unexplored) > 0:
        curPos, curDist = unexplored.pop(0)
                
        if curPos == goal:
            break
        
        nextPos = [(curPos[0]+1, curPos[1]),
                   (curPos[0]-1, curPos[1]),
                   (curPos[0], curPos[1]+1),
                   (curPos[0], curPos[1]-1)]
        
        for nPos in nextPos:
            if nPos[0] < 0 or nPos[0] >= grid.shape[0]:
                continue
            if nPos[1] < 0 or nPos[1] >= grid.shape[1]:
                continue
            if (nPos[0],nPos[1]) in explored:
                continue
            if grid[nPos[0], nPos[1]] == b'.':
                explored.add((nPos[0],nPos[1]))
                unexplored.append(((nPos[0], nPos[1]), curDist+1))
    
    # Change the grid
    grid[curPos] = b'G'
    grid[Gpos] = b'_'
    grid[Epos] = b'.'
    
    # Return the new grid and the number of steps it takes to move the data left
    return (grid, curDist+1) 
    
    
# Read and parse the input
f = open('input.txt', 'r')
diagnostics = f.read().split('\n')

# Parse nodes and count viable pairs
nodes = parse(diagnostics)
viablePairs = getViablePairs(nodes)

# Make the grid
grid = makeGrid(nodes)

# Count the number of steps to take the data to the top left
steps = 0
while grid[0,0] != b'G':
    grid, moveSteps = moveOneLeft(grid)
    steps += moveSteps
    
# Print the results
print(f'There are {viablePairs} viable pairs')
print(f'It takes {steps} steps to get the data to the top left')