# Heapque to do some dijkstra-ish stuff
import heapq

# Use a dijstra-ish function to get minimum heat loss, while
# only moving a maximum of three blocks in a single direction 
def find_best_path(layout, src):
    
    # Dict for the dists
    dists = {}
    
    # Because of the limit on moves in a single direction,
    # we add direction and a count on moves to the dist state
    dists[(src, (0,0), 0)] = 0
    
    queue = []
    
    # Add the starting position
    heapq.heappush(queue, (0, src, (0,0), float('inf')))
    
    # While there is stuff to do
    while len(queue) > 0:
    
        # Pop the next item
        dist, cur, direction, dirCount = heapq.heappop(queue)
        
        # For every direction
        for nextDir in [(1,0), (0,1), (-1, 0), (0, -1)]:
            
            # Calculate next direction
            x = cur[0] + nextDir[0]
            y = cur[1] + nextDir[1]
            
            # Check if we are out of bounds
            if x < 0 or x >= len(layout):
                continue
            if y < 0 or y >= len(layout[0]):
                continue
            
            # Check if we are going backwards from where we came
            if nextDir[0] == -direction[0] and nextDir[1] == -direction[1]:
                continue
            
            # Set the count on moves in the same direction
            count = dirCount + 1 if direction == nextDir else 1
                
            # If it is over three, continue to next item
            if count > 3:
                continue
                        
            # Add to dict to avoid key errors
            if ((x, y), nextDir, count) not in dists:
                dists[((x, y), nextDir, count)] = float('inf')
            
            # Calculate the new distance
            newDist = dist + int(layout[x][y])
            
            # If it is better than what we already have, add it to dict and push to queue
            if newDist < dists[((x,y), nextDir, count)]:
                dists[((x,y), nextDir, count)] = newDist
                heapq.heappush(queue, (newDist, (x,y), nextDir, count))
                
    return dists
        
# Similar function to above, but only allowing to move between 4 and 10 blocks
def ultra_find_best_path(layout, src):
    
    dists = {}
    dists[(src), (0,0), 0] = 0
    
    queue = []
    
    heapq.heappush(queue, (0, src, (0,0), float('inf')))
    
    while len(queue) > 0:
        
        dist, cur, direction, dirCount = heapq.heappop(queue)
        
        for nextDir in [(1,0), (0,1), (-1, 0), (0, -1)]:
        
            x = cur[0] + nextDir[0]
            y = cur[1] + nextDir[1]
            
            if x < 0 or x >= len(layout):
                continue
            if y < 0 or y >= len(layout[0]):
                continue
            if nextDir[0] == -direction[0] and nextDir[1] == -direction[1]:
                continue
            
            count = dirCount + 1 if direction == nextDir else 1
            
            if count > 10:
                continue
            
            if ((x, y), nextDir, count) not in dists:
                dists[((x, y), nextDir, count)] = float('inf')
                
            newDist = dist + int(layout[x][y])
            
            if newDist < dists[((x,y), nextDir, count)]:
            
                # If count is above 4, we can move freely
                if count > 4:
                    dists[((x,y), nextDir, count)] = newDist
                    heapq.heappush(queue, (newDist, (x,y), nextDir, count))
                    
                # If count is 4 or below, we can only move in the previous direction
                elif nextDir == direction:
                    dists[((x,y), nextDir, count)] = newDist
                    heapq.heappush(queue, (newDist, (x,y), nextDir, count))
                
                # If we are turning, previous direction count has to be above 3
                elif count == 1 and dirCount > 3:
                    dists[((x,y), nextDir, count)] = newDist
                    heapq.heappush(queue, (newDist, (x,y), nextDir, count))
                    
    return dists
                    

        

# Read and parse the input
f = open('input.txt', 'r')
layout = f.read().split('\n')

# Dictionary of losses from starting point
losses = find_best_path(layout, (0,0))

# Find the best one
min_loss = float('inf')
for l in losses:
    if l[0] == (len(layout)-1, len(layout[0])-1):
        if losses[l] < min_loss:
            min_loss = losses[l]
     
# Dictionary of losses from starting point, with the new crucibes
ultra_losses = ultra_find_best_path(layout, (0,0))

# Find the best one that we are allowed to stop at
ultra_min_loss = float('inf')
for l in ultra_losses:
    if l[0] == (len(layout)-1, len(layout[0])-1) and l[2] > 3:
        if ultra_losses[l] < ultra_min_loss:
            ultra_min_loss = ultra_losses[l]
        
# Print the results
print(f'The minimum heat loss is {min_loss}')
print(f'The minimum heat loss using ultra crucibes is {ultra_min_loss}')

