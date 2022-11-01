# Need numpy for fast array procesing
import numpy as np

# Return the number of neighbors that are currently on
def countNeighbours(lights, x, y):
    
    # Init zero, subtract one if light is on to offset the later calculation
    neighbors = 0
    if lights[x][y]:
        neighbors -= 1
    
    # Return the number of Trues in the 3x3 area around the coordinate
    # (apparently this is the fastest way to count Trues in a bool array)
    return neighbors + np.count_nonzero(lights[x-1:x+2, y-1:y+2])

# Gets the next iteration of the lights, based on the current one
def getNextStep(lights):
    
    # Make a deep copy of the array
    nextStep = np.copy(lights)
    
    # For every node
    for x in range(1, len(lights)-1):
        for y in range(1, len(lights[x])-1):
            
            neighbors = countNeighbours(lights, x, y)
            # If the light is on, check if we need to turn it off
            if lights[x][y] and not neighbors in [2,3]:
                nextStep[x][y] = False
            # If the light is off, check if we need to turn if on
            elif not lights[x][y] and neighbors == 3:
                nextStep[x][y] = True
        
    # Return the next iteration
    return nextStep
                
# Function for getting the next iteration if the lights in the corners are locked
def getNextStepLocked(lockedLights):
    
    # Get next iteration
    nextStep = getNextStep(lockedLights)
    
    # Turn all the corner lights on
    nextStep[1,1] = True
    nextStep[1,-2] = True
    nextStep[-2,1] = True
    nextStep[-2,-2] = True
    
    return nextStep

# Read the input file and parse it as a bool array
f = open('input.txt', 'r')
lights = [[True if c == '#' else False for c in l] for l in f.read().split('\n')]

# Pad the lights with false values to more easily count true neighbors
# on the edges
lights = np.pad(lights, [(1,1),(1,1)])

# Make a copy, where all the corners are on
lockedLights = np.copy(lights)
lockedLights[1,1] = True
lockedLights[1,-2] = True
lockedLights[-2,1] = True
lockedLights[-2,-2] = True

# The number of iterations
steps = 100
for i in range(steps):
    
    # Compute the next iteration for both lights
    lights = getNextStep(lights)
    lockedLights = getNextStepLocked(lockedLights)

# Print the results
print(f'{sum(sum(lights))} lights are on after {steps} iterations')
print(f'{sum(sum(lockedLights))} lights are on after {steps} iterations when the corners are always on')
