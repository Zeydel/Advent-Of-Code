# Need numpy for array stuff
import numpy as np

# Function for flashing an octopus
def flash(entries, x, y):
        
    # Set its value to zero and mark a flash
    entries[x,y] = 0
    flashes = 1
    
    # Go through neighbors and increment them, unless they have already flashed
    for l in range(x-1, x+2):
        for k in range(y-1, y+2):
            if entries[l,k] == 0:
                continue
            
            entries[l,k] += 1
            
            # If we increment a value to be 10, we flash that octopus
            if(entries[l, k] == 10):
                
                # Make recursive call to flash. Add return to number of flashes
                flashes += flash(entries, l, k)
                
    # Return number of flashes
    return flashes
    

# Open input, read as 2d array of ints. Pad with zeros
f = open('input.txt', 'r')
entries = np.array([[int(l) for l in list(line)] for line in f.read().split('\n')])
entries = np.pad(entries, pad_width=1, mode='constant', constant_values=0)

# Counter for number of flashes
total_flashes = 0

# Var for flashes after 100 steps
total_flashes_after_100 = 0

# Var for the first step where all octopodes flash
first_step_all_flash = -1

# Init current step to zero
s = 0

# While all octopi hasn't flashed at the same time
while first_step_all_flash == -1:
        
    # Increment all octopusses
    for i in range(1,entries.shape[0]-1):
        for j in range(1,entries.shape[1]-1):
            entries[i,j] = entries[i,j] + 1
    
    # Find all octos that should flash. Flash them and add to the number of flashes
    for i in range(1,entries.shape[0]-1):
        for j in range(1,entries.shape[1]-1):
            if entries[i,j] > 9:
                total_flashes += flash(entries, i, j)
                
    # Increment number of completed steps
    s += 1
    
    # If we are at 100 steps. Save current number of flashes
    if s == 100:
        total_flashes_after_100 = total_flashes
        
    # If all octopuser flashes, and we havent found a result for it yet, save the step number
    if first_step_all_flash == -1 and (entries == 0).all():
        first_step_all_flash = s
        
    
print('The total number of flashes after 100 steps is ' + str(total_flashes_after_100))
print('The first step where all octopuses flashes is ' + str(first_step_all_flash))