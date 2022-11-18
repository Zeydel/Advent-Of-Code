# Import a bunch of tools
import re
from copy import copy
from itertools import combinations

# Parse the floor info into a building
def parse(floors):
    
    # The building is a dictionary
    building = dict()
    
    # Every string contains info about a floor
    for i, f in enumerate(floors):
        
        # Init the dict entry with an empty array
        building[i] = []
        
        # Find all the generators and chips using regex
        generators = re.findall('([a-z]+) generator', f)
        microchips = re.findall('([a-z]+)-compatible microchip', f)
        
        # Add codes for found generators and chips to the floor
        # This parts assumes each element starts with a different letter
        for g in generators:
            building[i].append(g[0] + "G")   
        for m in microchips:
            building[i].append(m[0] + "M")
            
    # Return the building
    return building
  
# The possible moves for each floor
moves = {0: [1],
         1: [0,2],
         2: [1,3],
         3: [2]}

# Given a building, a depth and a elevator position, return a list of the
# next possible states
def getNextActions(building, depth, elevatorPos):
    
    # Init empty
    nextMoves = []
    
    # For 1 or 2 items in the elevator
    for i in range(1,3):
        # Find all combinations of that size
        combs = combinations(building[elevatorPos], i)
        for c in combs:
            # For every move (up or down)
            for m in moves[elevatorPos]:
                # Make a copy of the building
                move = copy(building)
                # Remove elements in combination from starting floor
                move[elevatorPos] = [e for e in move[elevatorPos] if e not in c]
                # And add them to the ending floor
                move[m] = move[m] + list(c)
                # Check that both floors are still valid
                if isValidFloor(move[elevatorPos]) and isValidFloor(move[m]):
                    # Add the move to the list of next possible states
                    nextMoves.append((move, depth+1, m))
    
    # Return the list of next states
    return nextMoves

# Represent the building using strings
def buildingToString(building, elevatorPos):
    
    # Start with the elevator position
    string = str(elevatorPos)
    
    # For every floor
    for f in building:
        # Add the floor
        string += str(f)
        displacements = []
        # For every element
        for e in building[f]:
            # If it is a chip
            if e[1] == 'M':
                # Find its generator
                for f in building:
                    if e[0] + 'G' in building[f]:
                        # Add that we have found a chip, plus the floor
                        # that its generator was found on.
                        # The specific chip doesn't matter
                        displacements.append('M' + str(f))
        
        # Add the sorted list of displacements to the string
        string += ''.join(sorted(displacements))
                        
    return string
                       
# Checks that a floor is valid 
def isValidFloor(floor):
    # For every element
    for e in floor:
        # If it is a microchip, its generator is not on the floor, and there is another generator on the floor
        if e[1] == 'M' and e[0] + 'G' not in floor and any([g[1] == 'G' for g in floor]):
            return False
    return True

# Checks that all floors except the top one is empty
def isFinal(building):
    return len(building[0]) == 0 and len(building[1]) == 0 and len(building[2]) == 0

# Given a building, finds the minimum steps to get all elements to the top
def findMinSteps(building):
    
    # Start with the inital state. Depth and elevatorpos are both zero
    states = [(building, 0, 0)]
    
    # Keep a set of explored states
    explored = set()
    
    # While we have states left to explore
    while len(states) > 0:
        # Get the first state in the list (we are doing BFS)
        building, depth, elevatorPos = states.pop(0)
            
        # Get the string representation of the building
        bts = buildingToString(building, elevatorPos)
        # If we have seen it before, skip this iteration
        if bts in explored:
            continue
        
        # Else add the string representation to the set of explored states 
        explored.add(bts)
        
        # If we have reached the goal, return the depth
        if isFinal(building):
            return depth;
            
        # Add the next possible states to the queue
        states += getNextActions(building, depth, elevatorPos)
        
    # If we havent found a solution, return infinite
    return float('inf')


# Open input and read as strings
f = open('input.txt', 'r')
floors = f.read().split('\n')

# Parse the building
building = parse(floors)

# Find the minimum number of steps
best = findMinSteps(building)
    
# Add the new elements to the building and find the new minimum number of steps
building[0] = sorted(building[0] + ['eG', 'eM', 'dG', 'dM'])
bestMoreElements = findMinSteps(building)

# Print the results
print(f'The fewest steps to reach the top with all elements is {best}')    
print(f'The fewest steps to reach the top with more elements is {bestMoreElements}')
    
    
    
    
    
    
    
    