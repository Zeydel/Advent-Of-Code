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
                if isValidFloor(move[elevatorPos]) and isValidFloor(move[m]):
                    nextMoves.append((move, depth+1, m))
                
    return nextMoves
      
def buildingToString(building, elevatorPos):
    
    string = str(elevatorPos)
    
    for f in building:
        string += str(f) + ''.join(sorted(building[f]))
        
    return string

def isValid(building):
    
    for f in building:
        for e in building[f]:
            if e[1] == 'M' and e[0] + 'G' not in building[f] and any([g[1] == 'G' for g in building[f]]):
                return False
            
    return True

def isValidFloor(floor):
    for e in floor:
        if e[1] == 'M' and e[0] + 'G' not in floor and any([g[1] == 'G' for g in floor]):
            return False
    return True

def isFinal(building):
    
    return len(building[0]) == 0 and len(building[1]) == 0 and len(building[2]) == 0


# Open input and read the string
f = open('input.txt', 'r')
floors = f.read().split('\n')

building = parse(floors)
originalBuilding = copy(building)

states = [(building, 0, 0)]
explored = dict()
best = float('inf')
best2 = float('inf')

while len(states) > 0:
    building, depth, elevatorPos = states.pop(0)
    
    if depth >= best:
        continue
    
    bts = buildingToString(building, elevatorPos)
    if bts in explored and explored[bts] <= depth:
        continue
    
    explored[bts] = depth
    
    if isFinal(building) and depth < best:
        best = depth
        
    states += getNextActions(building, depth, elevatorPos)
    
building = originalBuilding
building[0] = sorted(building[0] + ['eG', 'eM', 'dG', 'dM'])
explored = dict()
states = [(building, 0, 0)]
maxDepth = 0

while len(states) > 0:
    building, depth, elevatorPos = states.pop()
    
    if depth >= best:
        continue
    
    bts = buildingToString(building, elevatorPos)
    if bts in explored and explored[bts] <= depth:
        continue
    
    explored[bts] = depth
    
    if isFinal(building) and depth < best2:
        best2 = depth
        
    states += getNextActions(building, depth, elevatorPos)

    print(depth)
print(best)
print(best2)
    
    
    
    
    
    
    
    