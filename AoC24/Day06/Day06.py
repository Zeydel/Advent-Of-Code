# Parse the input into a set of obstacles and a starting position
def parse(lines):
    
    starting_pos = (-1, -1)
    obstacles = set()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char == '^':
                starting_pos = (x, y)
            
            if char == '#':
                obstacles.add((x,y))
                
    return obstacles, starting_pos
    
# Check wether a position is within the bounds of the map
def is_in_bound(x, y, lines):
    
    if y < 0 or y >= len(lines):
        return False
    
    if x < 0 or x >= len(lines[y]):
        return False
    
    return True
        
# Given a starting position and a number of obstacles, get the set of
# nodes that will be visited
def get_visited_nodes(starting_pos, obstacles):
    
    # The sequence of moving directions
    dirs = [(0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)]
    
    # Initially, we are going up
    cur_dir = 0
    
    # Start at the given position
    pos = starting_pos
    
    # Init empty set of visited nodes
    visited = set()
    
    # While we are in bounds
    while is_in_bound(pos[0], pos[1], lines):
        
        # Add current position to the set of visited nodes
        visited.add(pos)
        
        # Calculate next position
        d_pos = (pos[0] + dirs[cur_dir][0], pos[1] + dirs[cur_dir][1])
        
        # If next pos is an obstacle, change directions
        if d_pos in obstacles:
            cur_dir += 1
            cur_dir %= len(dirs)
            
        # Otherwise move to next direction
        else:
            pos = d_pos
            
    # Return set of visited nodes
    return visited


# Check whether a loop occurrs given a starting position and a list of obstacles
def is_looping(starting_pos, obstacles):
    
    # The sequence of directions
    dirs = [(0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)]
    
    # Current direction
    cur_dir = 0
    
    # Start at the given position
    pos = starting_pos
    
    # Set of visited nodes
    visited = set()
    
    # While we are in bounds
    while is_in_bound(pos[0], pos[1], lines):
        
        # If we have been at the current position before
        # while facing the same direction, we are in a loop
        if (pos[0], pos[1], cur_dir) in visited:
            return True
        
        # Add current position, including direction to the set
        visited.add((pos[0], pos[1], cur_dir))
        
        # Move
        d_pos = (pos[0] + dirs[cur_dir][0], pos[1] + dirs[cur_dir][1])
        
        if d_pos in obstacles:
            cur_dir += 1
            cur_dir %= len(dirs)
        else:
            pos = d_pos
            
    # If we are outside the bounds of the map, there are no loops
    return False

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
obstacles, starting_pos = parse(lines)

# Get visited nodes and count them
visited_nodes = get_visited_nodes(starting_pos, obstacles)

visited_nodes_count = len(visited_nodes)

# Init var to store number of loops
loop_count = 0

# For every node visited except for starting position, check if placing
# an obstacle there causes a loop. Increment count if so
for node in visited_nodes.difference(starting_pos):
    
    if is_looping(starting_pos, obstacles.union({node})):
        loop_count += 1

# Print the results
print(f'{visited_nodes_count} nodes are visited by the guard')
print(f'{loop_count} obstacle placement would cause loop')