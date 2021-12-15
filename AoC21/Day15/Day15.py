# Import numpy for array stuff
import numpy as np

# Function to get adjecent nodes for a node
def get_adjecent(risk_levels, y, x):
    adjecent = []
    
    # Check if we are at the edge. If not add the node
    if y > 0:
        adjecent.append((y - 1, x))

    if x > 0:
        adjecent.append((y, x - 1))
        
    if y < risk_levels.shape[0]-1:
        adjecent.append((y + 1, x))
        
    if x < risk_levels.shape[1]-1:
        adjecent.append((y, x + 1))
        
    # Return the list
    return adjecent

# Function to get total risk levels for all cells
def get_total_risk_levels(risk_levels):
    
    # Create a new array and fill it with infinitys
    total_risk = np.zeros((risk_levels.shape[0], risk_levels.shape[1]), dtype = float)
    total_risk.fill(float('inf'))
    
    # Starting risk is 0
    total_risk[0,0] = 0
        
    # Add starting location to list of next nodes
    next_nodes = [(0,0)]

    # While list is not empty
    while next_nodes:
        
        # Pop from the beginning of queue
        n = next_nodes.pop(0)
        
        # Get adjecent nodes
        adjecent = get_adjecent(risk_levels, n[0], n[1])
    
        # For each adjecent node
        for a in adjecent:
            
            # Calculate the risk
            dist = risk_levels[a[0], a[1]] + total_risk[n[0], n[1]]
            
            # Update if we have found a new best risk and add to next nodes
            if dist < total_risk[a[0], a[1]]:
                total_risk[a[0], a[1]] = dist
                next_nodes.append((a[0], a[1]))
            
            
    # Return the calculated risks
    return total_risk

# Function to get the larger cave
def get_larger_cave(entries):
    
    # Make a copy of the original cave
    entries_copy = entries.copy()
    
    # Repeat four times
    for _ in range(4):
        
        # Create a new cave by incrementing or setting to zero
        entries_copy = np.array([[1 if i == 9 else i + 1 for i in j] for j in entries_copy])
        
        # Append to original cave
        entries = np.append(entries, entries_copy, axis = 1)

    # Repeat for other dimension
    entries_copy = entries.copy()
    for _ in range(4):
        entries_copy = np.array([[1 if i == 9 else i + 1 for i in j] for j in entries_copy])
        
        entries = np.append(entries, entries_copy, axis = 0)
        
    # Return the new cave
    return entries

    
    

# Open input, read as 2d array of ints. Pad with zeros
f = open('input.txt', 'r')
entries = np.array([[int(l) for l in list(line)] for line in f.read().split('\n')])

# Get risks for the caves
risks = get_total_risk_levels(entries)

# Find the minimum risk of the last element
min_risk = int(risks[-1,-1])

# Create the new, bigger cave
new_cave = get_larger_cave(entries)

# Find the risks for the large cave
risks_large_cave = get_total_risk_levels(new_cave)

# Find the minimum risk of the last element in the large cave
min_risk_large_cave = int(risks_large_cave[-1,-1])

# Print the result
print('The minimum risk of traversing the cave is ' + str(min_risk))
print('The minimum risk of traversing the large cave is ' + str(min_risk_large_cave))
