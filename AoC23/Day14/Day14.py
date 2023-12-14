# Class representing a node with its contents, load, and neighbors
class Node:
    
    def __init__(self, contents, load):
        self.contents = contents
        self.load = load
        
        self.neighbors = {}
      
# Parse the rock map into a grid graph
def parse(rockMap):
    
    # Dict to keep track of discovered nodes
    nodes = {}
    
    for i, line in enumerate(rockMap):
        
        # Calculate the load
        load = len(rockMap) - i
        
        # Create a node for each line
        for j, c in enumerate(line):
            node = Node(c, load)
            
            # Find east neighbors
            if i > 0:
                north = get_neighbor(nodes, rockMap, i-1, j)
                node.neighbors['N'] = north
                north.neighbors['S'] = node
                nodes[(i-1, j)] = north
            if j > 0:
                west = get_neighbor(nodes, rockMap, i, j-1)
                node.neighbors['W'] = west
                west.neighbors['E'] = node
                nodes[(i, j-1)] = west
            if i < len(rockMap) - 1:
                south = get_neighbor(nodes, rockMap, i+1, j)
                node.neighbors['S'] = south
                south.neighbors['N'] = node
                nodes[(i+1,j)] = south
            if j < len(line) - 1:
                east  = get_neighbor(nodes, rockMap, i, j+1)
                node.neighbors['E'] = east
                east.neighbors['W'] = node
                nodes[(i,j+1)] = node
                
            nodes[(i,j)] = node
            
    return nodes[(0,0)], nodes[(len(rockMap)-1, len(line)-1)]
            
# If node is already in dict, add it directly. Otherwise creat it
def get_neighbor(nodes, rockMap, i, j):
    if (i,j) in nodes:
        return nodes[(i,j)]
    
    load = len(rockMap) - 1
    contents = rockMap[i][j]
    node = Node(contents, load)
    
    return node

# Run a spin cycle
def spin_cycle(upper_left, lower_right):
    
    upper_left, lower_right = slide(upper_left, lower_right, 'N')
    upper_left, lower_right = slide(upper_left, lower_right, 'W')
    upper_left, lower_right = slide(upper_left, lower_right, 'S')
    upper_left, lower_right = slide(upper_left, lower_right, 'E')
    
    return upper_left, lower_right
    
# Slide all rocks in a direction
def slide(upper_left, lower_right, direction):

    # The sliding direction influences the order in which we have to add neighbors
    add = {'N': ['S', 'E'],
           'W': ['E', 'S'],
           'S': ['N', 'W'],
           'E': ['W', 'N']}

    
    explored = set()
    stack = []
    
    # The sliding direction influences the starting node
    if direction in ('N', 'W'):
        stack.append(upper_left)
    else:
        stack.append(lower_right)
      
    # Do a DFS, and slide rocks every time we meet it
    while len(stack) != 0:
        
        cur = stack.pop()
        explored.add(cur)
        
        for a in add[direction]:
            
            if a in cur.neighbors != None and cur.neighbors[a] not in explored:
                stack.append(cur.neighbors[a])
                
        if cur.contents in ('.', '#'):
            continue
        
        while direction in cur.neighbors != None and cur.neighbors[direction].contents == '.':
            cur.neighbors[direction].contents = 'O'
            cur.contents = '.'
            cur = cur.neighbors[direction]
            
    return upper_left, lower_right
    
# Function to get the total load using a DFS
def get_total_load(upper_left):
    
    total_load = 0
    
    explored = set()
    stack = [upper_left]
    
    while len(stack) != 0:
        
        cur = stack.pop()
        explored.add(cur)
        
        for a in ['S', 'E']:
            
            if a in cur.neighbors != None and cur.neighbors[a] not in explored:
                stack.append(cur.neighbors[a])
                
        if cur.contents in ('.', '#'):
            continue
        
        total_load += cur.load
            
    return total_load
    
# Identify a loop in the list of loads
def get_loop_length(loads, value):
    
    # If the value is not yet in the list of loops, we dont have a loop
    if value not in loads:
        return -1, []
        
    # The index of the last occurence of the element in the list
    last_index = len(loads) - loads[::-1].index(value) - 1
    
    # The last element of the list, before the new value is added to the lsit
    cur = len(loads) - 1
    prev = last_index - 1
    
    # If the last occurence was the previous element, it is not a loop
    if cur - prev == 1:
        return -1, []
    
    # Check from current index until last index. If all elements matches, it is a loop
    while cur > last_index and prev > 0:
        
        if loads[cur] != loads[prev]:
            return -1, []
        
        cur -= 1
        prev -= 1
        
    # Return the last index and the loop
    return last_index, loads[last_index:]
        
    
    

# Read and parse the input
f = open('input.txt', 'r')
rockMap = f.read().split('\n')

# Parse the map
upper_left, lower_right = parse(rockMap)

# Calculate the initial load
loads = [get_total_load(upper_left)]

# Slide north
upper_left, lower_right = slide(upper_left, lower_right, 'N')

# Calculate load gain
loadNorth = get_total_load(upper_left)

# Vars for the spin cycles
loop = []
loop_start = -1
cycles = 1000000000

# Run the cycles
for i in range(cycles):
    upper_left, lower_right = spin_cycle(upper_left, lower_right)
    
    # Calculate the load
    load = get_total_load(upper_left)
    
    # Try to find a loop
    loop_start, loop = get_loop_length(loads, load)
        
    # If we have found a loop, break the loop
    if loop != []:
        break
    
    # Otherwise append to list and continue
    loads.append(get_total_load(upper_left))

# Use some fancy maths to find the value after the spin cycles
cycles -= (loop_start)
cycles %= len(loop)
loadSpinCycle = loop[cycles]

# Print the results
print(f'The load after tilting north is {loadNorth}')
print(f'The load after the spin cycles is {loadSpinCycle}')

#print(get_total_load(upper_left))