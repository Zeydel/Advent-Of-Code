import re
from itertools import permutations
import numpy as np

def parse(diagnostics):
    nodes = []
    
    for d in diagnostics[2:]:
        s = d.split()
        
        x = int(re.findall(r'x(\d+)', s[0])[0])
        y = int(re.findall(r'y(\d+)', s[0])[0])
        
        size = int(s[1][:-1])
        used = int(s[2][:-1])
        avail = int(s[3][:-1])
        use = int(s[4][:-1])
        
        nodes.append([x, y, size, used, avail, use])
        
    return nodes
        
def makeGrid(nodes):
    maxX = max(n[0] for n in nodes)
    maxY = max(n[1] for n in nodes)
    
    grid = np.chararray((maxY+1, maxX+1))
    
    for n in nodes:
        if n[3] > 150:
            grid[n[1],n[0]] = '#'
        elif n[3] == 0:
            grid[n[1],n[0]] = '_'
        else:
            grid[n[1],n[0]] = '.'
    
    grid[0, maxX] = 'G'
    
    return grid

def isViable(A, B):
    if A[5] == 0:
        return False
    
    if A[3] > B[4]:
        return False
    
    return True

def getViablePairs(nodes):
    
    pairCount = 0
    for c in permutations(nodes, 2):
        if isViable(c[0], c[1]):
            pairCount += 1
            
    return pairCount
        
    
# Read and parse the input
f = open('input.txt', 'r')
diagnostics = f.read().split('\n')

nodes = parse(diagnostics)
grid = makeGrid(nodes)


print(getViablePairs(nodes))
