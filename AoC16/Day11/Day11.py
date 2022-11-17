import re
from copy import copy
from itertools import combinations

def parse(floors):
    
    building = dict()
    
    for i, f in enumerate(floors):
        
        building[i] = []
        
        generators = re.findall('([a-z]+) generator', f)
        microchips = re.findall('([a-z]+)-compatible microchip', f)
        
        for g in generators:
            building[i].append(g[0] + "G")
            
        for m in microchips:
            building[i].append(m[0] + "M")
            
    return building
  
moves = {0: [1],
         1: [0,2],
         2: [1,3],
         3: [2]}
def getNextActions(building, depth, elevatorPos):
    
    nextMoves = []
    
    for i in range(1,3):
        combs = combinations(building[elevatorPos], i)
        for c in combs:
            for m in moves[elevatorPos]:
                move = copy(building)
                move[elevatorPos] = [e for e in move[elevatorPos] if e not in c]
                move[m] = sorted(move[m] + list(c))
                nextMoves.append((move, depth+1, m))
                
    return nextMoves
      
def buildingToString(building):
    
    string = ''
    
    for f in building:
        string += str(f) + ''.join(sorted(building[f]))
        
    return string

def isValid(building):
    
    for f in building:
        for e in building[f]:
            if e[1] == 'M' and e[0] + 'G' not in building[f] and any([g[1] == 'G' for g in building[f]]):
                return False
            
    return True

# Open input and read the string
f = open('input.txt', 'r')
floors = f.read().split('\n')

building = parse(floors)

states = [(building, 0, 0)]

test = getNextActions(building, 0, 0)

for s in test:
    print(buildingToString(s[0]))
    print(isValid(s[0]))
    print()

while len(states) > 0:
    building, depth, elevatorPos = states.pop(0)
    
    if not isValid(building):
        continue
    
    
    
    