import math
from heapq import heappush, heappop

# Parse the input into a list of tuples
def parse(lines):
    
    boxes = []
    
    for line in lines:
        
        x, y, z = line.split(',')
        
        boxes.append((int(x), int(y), int(z)))
        
    return boxes

# Get the distance between two boxes
def get_distance(b1, b2):
    
    return math.sqrt(math.pow(b1[0] - b2[0], 2) + math.pow(b1[1] - b2[1], 2) + math.pow(b1[2] - b2[2], 2))

# Get the pairwise distances between all boxes in a prioritised heap
def get_all_distances(boxes):
    
    distances = []
    
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            
            dist = get_distance(boxes[i], boxes[j])
            
            heappush(distances, (dist, boxes[i], boxes[j]))
            
    return distances

# Make a given number of connections
def make_connections(boxes, distances, connections):

    # Make a group for each box, and register the group that each box belongs to
    groups = {i: {box} for i, box in enumerate(boxes)}
    parents = {box: i for i, box in enumerate(boxes)}

    distance_copy = distances
    
    # Initially, we have made zero connections
    connections_made = 0
    
    # While there are connections to be made
    while connections_made < connections:
        
        # Increment counter
        connections_made += 1
        
        # Get the next shortest distance
        dist, b1, b2 = heappop(distance_copy)
        
        # If the boxes belong to the same group, dont do anything
        if parents[b1] == parents[b2]:
            continue
        
        # Remeber the previous parent of the first group
        prev_parent = parents[b1]
        
        # Get the boxes that should be moved from the first group
        to_move = groups[parents[b1]]
        
        # Add them to the second group
        groups[parents[b2]] |= to_move
        
        # Update parent for all moved boxes
        for b in to_move:
            parents[b] = parents[b2]
                                    
        # Remove the old group
        del groups[prev_parent]
        
    # Return the new groups
    return groups
        
# The same as above, but continue until there is only one group left
# Return the two last connected boxes
def get_last_connections(boxes, distances):
    
    groups = {i: {box} for i, box in enumerate(boxes)}
    parents = {box: i for i, box in enumerate(boxes)}
    
    while len(groups) != 1:
        
        dist, b1, b2 = heappop(distances)
        
        if parents[b1] == parents[b2]:
            continue
        
        prev_parent = parents[b1]
        
        to_move = groups[parents[b1]]
        
        groups[parents[b2]] |= to_move
        
        for b in to_move:
            parents[b] = parents[b2]
                                    
        del groups[prev_parent]
        
    return b1, b2

# Given the groups, return the product of the sizes of the three
# largets groups
def get_largets_circuit_product(groups):
    
    sizes = [len(groups[k]) for k in groups]
    
    sizes = sorted(sizes)[::-1]
    
    return sizes[0] * sizes[1] * sizes[2]

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
boxes = parse(lines)

# Get all distances
distances = get_all_distances(boxes)

# Init connection number
connections = 1000

# Get groups after making given number of connections
groups = make_connections(boxes, distances, connections)

# Get the product of the sizes of the largest groups
product = get_largets_circuit_product(groups)

# Get final boxes connected after making all connections
b1, b2 = get_last_connections(boxes, distances)

print(f'The product of the three largest groups is {product}')
print(f'The product of the x coordinates of the two last connected boxes is {b1[0] * b2[0]}')