# Yeah, this one took a few days to figure out...
import numpy as np

# Function to spawn a rock
def spawn(tunnel, rocks, rockNumber, wind, idx, spawnPos):
    
    # If the tunnel is currently too short, add some more rows on top
    if tunnel.shape[0] < spawnPos+4:
        tunnel = np.vstack([tunnel, np.zeros((spawnPos+4-tunnel.shape[0],7),dtype=bool)])
        
    # Get the current rock to spawn
    rock = list(rocks[rockNumber])
            
    # Add it to the spawn position (we spawn it one unit above the top instead of 3)
    for i in range(len(rock)):
        rock[i] = (rock[i][0]+spawnPos,rock[i][1]+spawnPos)
        
    # Rocks starts 2 units in
    start = 2    
    
    # Apply the first four winds
    for i in range(4):
        
        if wind[idx] == '<':
            start = max(0, start-1)
        else:
            start = min(7-len(rock), start+1)
        idx += 1
        idx %= len(wind)
    
    # Determine the rocks vertical position
    rock = [-1]*start + rock + (7-start-len(rock))*[-1]
           
    
    # Move around until settles
    while True:
        
        # Check if we are settled
        settled = False
        for i, r in enumerate(rock):
            if r == -1:
                continue
            if rock[i][0] == 0 or tunnel[rock[i][0]-1,i]:
                settled = True
                break
                
        # If we are settled, break
        if settled:
            break
        
        # Move down
        newRock = []
        for r in rock:
            if r == -1:
                newRock.append(-1)
                continue
            newRock.append((r[0]-1, r[1]-1))
            
        rock = newRock
            
        # Apply wind
        move = 0
        
        if wind[idx] == '<' and rock[0] == -1:            
            move = -1
        elif wind[idx] == '>' and rock[-1] == -1:
            move = 1
            
        idx += 1
        idx %= len(wind)
        canMove = True    
        
        if move != 0:
            for i, r in enumerate(rock):
                if r == -1:
                    continue
                for p in range(r[0],r[1]+1):
                    if tunnel[p, i+move]:
                        canMove = False
                        break
                        
            if canMove:
                if move == -1:
                    rock = rock[1:] + [rock[0]]
                if move == 1:
                    rock = [rock[-1]] + rock[:-1]
                
        
        
    # Once rock is settled, update the tunnel
    for i, r in enumerate(rock):
        if r == -1:
            continue
        
        tunnel[r[0]:r[1]+1, i] = True
        
        if r[1]+1 > spawnPos:
            spawnPos = r[1]+1
      
    # Return the tunnel, wind index and spawn height
    return (tunnel, idx, spawnPos)
        

# Open input and read as strings
f = open('input.txt', 'r')
wind = f.read()

# The 5 different rock types
rocks = {
    0: [(0,0),(0,0),(0,0),(0,0)],
    1: [(1,1),(0,2),(1,1)],
    2: [(0,0),(0,0),(0,2)],
    3: [(0,3)],
    4: [(0,1),(0,1)]
    }
        
# Create the tunnel
tunnel = np.zeros((4,7),dtype=bool)

# Index and spawnheight start at zero
idx = 0
spawnPos = 0

# For the first one, just calculate it outright
for i in range(2022):
        
    tunnel, idx, spawnPos = spawn(tunnel, rocks, i%5, wind, idx, spawnPos)

# Save the height
after2022 = max(np.where(tunnel == True)[0])+1

# Create a new tunnel
tunnel = np.zeros((4,7),dtype=bool)

# Same indeces as before
idx = 0
spawnPos = 0

# Var for the final height
height = 0

# Var for the target number of iterations
target = 1000000000000

# Dict of the wind indeces we have seen
seen = dict()

# Var for the wind index to use for calculating height
use = -1

# Start by just running it
for i in range(target):
   
    # For the first 100 indecies (except zero)
    if idx < 100 and idx > 0:
        
        # If we have not seen the index before, add it to the dict
        if idx not in seen:
            seen[idx] = []
        
        # Add the current iteration and height to the dict
        seen[idx].append((i, max(np.where(tunnel == True)[0])+1))
    
        # If we have seen an index more than 20 times
        if len(seen[idx]) > 20:
            
            # And the intervals are perfectly regular
            if all([seen[idx][1][0] - seen[idx][0][0] == seen[idx][j+1][0] - seen[idx][j][0] for j in range(len(seen[idx])-1)]):
                if all([seen[idx][1][1] - seen[idx][0][1] == seen[idx][j+1][1] - seen[idx][j][1] for j in range(len(seen[idx])-1)]):
                    
                    # We can use the index for calculations
                    use = idx
        
        # If we have an index we can use, we can calculate the final height
        if use != -1:
            
            # The height until the interval starts
            height += seen[use][0][1]
            
            # Calculate interval lengths and heights
            intervalLen = seen[use][1][0] - seen[use][0][0]
            intervalSum = seen[use][1][1] - seen[use][0][1]
            
            # And the number of intervals we can fit in the remaining space
            numIntervals = (target-seen[use][0][0])//intervalLen
            
            # Add the number of intervals times the height for each interval
            height += (numIntervals*intervalSum)
            
            # Find out how many iterations we need after the first two parts
            remaining = (target-seen[use][0][0])-(numIntervals*intervalLen)

            # Calculate the current height
            past = max(np.where(tunnel == True)[0])+1
            
            # Calculate the final part outright
            for j in range(remaining):
                tunnel, idx, spawnPos = spawn(tunnel, rocks, (i+j)%5, wind, idx, spawnPos)
            
            # Calculate the height again
            cur = max(np.where(tunnel == True)[0])+1
            
            # Add the final part to the height
            height += cur-past
            
    # If we have found a height, we are done
    if height != 0:
        break
         
    # Run an iteration
    tunnel, idx, spawnPos = spawn(tunnel, rocks, i%5, wind, idx, spawnPos)

        
# Print the results
print(f'After 2022 rock, the tower is {after2022} units high')
print(f'After 1000000000000 rocks, the tower is {height} units high')