# I need my tools
import numpy as np
from itertools import permutations

# Function to get all dists from one node to every other target
def getAllDists(current, targets, grid):
    
    # Make a dict. Zero steps to current placement
    dists = dict()
    dists[current] = 0
    
    # Find the current node
    Gpos = np.where(grid == current)
    Gcord = list(zip(Gpos[0], Gpos[1]))[0]

    # Do a BFS for all other nodes
    unexplored = [(Gcord, 0)]
    explored = set()
    explored.add(Gcord)
    
    while len(dists) < len(targets):
        curPos, curDist = unexplored.pop(0)
        
        if grid[curPos] in targets:
            dists[grid[curPos]] = curDist
        
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
            if grid[nPos[0], nPos[1]] != '#':
                explored.add((nPos[0],nPos[1]))
                unexplored.append(((nPos[0], nPos[1]), curDist+1))
    
    # Return the dists
    return dists


# Open input and read as strings
f = open('input.txt', 'r')
grid = np.array([list(l) for l in f.read().split('\n')])

# Find all the numbers
targets = []
t = 0
while str(t) in grid:
    targets.append(str(t))
    t += 1
    
# Find dists for all numbers
dists = []
for i in range(len(targets)):
    dists.append(getAllDists(str(i), targets, grid))

# Overestimate the best
best = float('inf')    

# Find all permutations
for p in permutations(targets[1:]):
    
    # Sum up the distances
    dist = dists[0][p[0]]
    for i in range(0, len(p)-1):
        
        dist += dists[int(p[i])][p[i+1]]
        
    # If we have beat the best, save it
    if dist < best:
        best = dist
        
# Do the same thing again, but this time return to start
bestReturn = float('inf')

for p in permutations(targets[1:]):

    dist = dists[0][p[0]]

    for i in range(0, len(p)-1):

        dist += dists[int(p[i])][p[i+1]]
        
    dist += dists[int(p[i+1])]['0']
    
    if dist < bestReturn:
        bestReturn = dist

# Print the results
print(f'The fewest number of steps is {best}')
print(f'If we have to return, the fewest number of steps is {bestReturn}')