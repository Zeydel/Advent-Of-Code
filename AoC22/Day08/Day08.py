# Things are just easier in np arrays
import numpy as np

# Function to check if a tree is visible from the edges
def isVisible(x, y, trees):
    
    # Extract the value of a tree
    val = trees[x,y]
    
    # Check all directions. If it is visible return true
    if all([val > t for t in trees[x,y+1:]]):
        return True
    
    if all([val > t for t in trees[x,:y]]):
        return True
    
    if all([val > t for t in trees[x+1:,y]]):
        return True
    
    if all([val > t for t in trees[:x,y]]):
        return True
    
    # Otherwise return false
    return False
    
# Get the viewing distance for a tree
def getViewingDistance(x, y, trees):
    
    # Functions for each direction
    u, d, l, r = 0, 0, 0, 0
    
    # Extract the value
    val = trees[x,y]
    
    # For every direction, check along it until we can no longer see
    # Then break the loop
    for i in range(y+1, trees.shape[1]):
        r += 1
        if trees[x, i] >= val:
            break
        
    for i in range(y-1, -1, -1):
        l += 1
        if trees[x, i] >= val:
            break
        
    for i in range(x+1, trees.shape[0]):
        d += 1
        if trees[i, y] >= val:
            break
        
    for i in range(x-1, -1, -1):
        u += 1
        if trees[i, y] >= val:
            break
    
    # Return the product
    return u*d*l*r

# Open input and read as strings
f = open('input.txt', 'r')
trees = f.read().split('\n')

# Turn the input into a np array
trees = np.array([list(i) for i in trees], dtype=int)

# Start by adding all the edge trees to the visible sum
visible = (2*trees.shape[0])+ (2*(trees.shape[1]-2))

# Init var for best viewing distance
best = 0

# For every tree not on the edges
for x in range(1, trees.shape[0]-1):
    for y in range(1, trees.shape[1]-1):
       
        # Check if it is visible
        if isVisible(x, y, trees):
            visible += 1
            
        # Find the viewing distance and update best if necesarry
        vd = getViewingDistance(x, y, trees)
        if vd > best:
            best = vd
        
# Print the results
print(f'{visible} trees are visible')
print(f'The best viewing distance is {best}')