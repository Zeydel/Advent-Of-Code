# Need numpy for array stuff
import numpy as np

# Basically floodfill with a counter
def get_basin_size_and_mark(entries, marks, i, j):
    
    # Mark current placement
    marks[i,j] = True
    
    # Init size
    size = 1
    
    # If any direction has not been marked, recursively call the function and add result to size
    if not marks[i-1,j]:
        size += get_basin_size_and_mark(entries, marks, i-1, j)
    if not marks[i+1,j]:
        size += get_basin_size_and_mark(entries, marks, i+1, j)
    if not marks[i,j-1]:
        size += get_basin_size_and_mark(entries, marks, i, j-1)
    if not marks[i,j+1]:
        size += get_basin_size_and_mark(entries, marks, i, j+1)
        
    # Return the size
    return size
        
# Open file, read input as 2d np array and pad it with value 100
f = open('input.txt', 'r')
entries = np.array([[int(l) for l in list(line)] for line in f.read().split('\n')])
entries = np.pad(entries, pad_width=1, mode='constant', constant_values=100)

# Init counter for risk level
risk_levels = 0

# Create a shadow array to signify if an entry has been marked
marked = np.zeros((entries.shape[0], entries.shape[1]), dtype=bool)

# Go trough the entries and mark values 9 and above
for i in range(entries.shape[0]):
    for j in range(entries.shape[1]):
        if entries[i,j] >= 9:
            marked[i,j] = True

# List of basin sizes
basin_sizes = []

# Go trough array (except for borders)
for i in range(1,entries.shape[0]-1):
    for j in range(1,entries.shape[1]-1):
        
        # If current entry has not been marked, find the basin size and add it to list
        if not marked[i,j]:
            basin_sizes.append(get_basin_size_and_mark(entries,marked, i,j))
            
        # Continue loop if entry is not a low point
        if not entries[i,j] < entries[i-1,j]:    
            continue
        if not entries[i,j] < entries[i,j-1]:    
            continue             
        if not entries[i,j] < entries[i,j+1]:    
            continue            
        if not entries[i,j] < entries[i+1,j]:    
            continue
        
        # Add the risk level to the sum
        risk_levels += entries[i,j] + 1

# Sport the list of basin sizes            
basin_sizes = sorted(basin_sizes)
product_of_largest_sizes = basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]

print('The sum of risk levels is ' + str(risk_levels))
print('The product of the three largest basin sizes is ' + str(product_of_largest_sizes))