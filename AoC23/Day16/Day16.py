# Class representing a node in the grid
class Node:
    
    def __init__(self):
        self.directions = {}
    
# Parse the grid into a graph-ish structure
def parse(layout):
    
    # Empty layout of grid
    nodeLayout = []
    
    # For every line
    for i, l in enumerate(layout):
        
        layoutLine = []
        
        # For every tile
        for j, c in enumerate(l):
            
            # Create a node
            node = Node()
            
            # If the beam should not just continue forwards, define its new direction
            if c == '\\' :
                node.directions = {(0,1):  [(1,0)],
                                   (1,0):  [(0,1)],
                                   (0,-1): [(-1,0)],
                                   (-1,0): [(0,-1)]}
            elif c == '/':
                node.directions = {(0,1):  [(-1,0)],
                                   (-1,0): [(0,1)],
                                   (0,-1): [(1,0)],
                                   (1,0):  [(0,-1)]}
            elif c == '|':
                node.directions = {(0,1):  [(1,0), (-1,0)],
                                   (0,-1): [(1,0), (-1,0)]}
            elif c == '-':
                node.directions = {(1,0):  [(0,1), (0,-1)],
                                   (-1,0): [(0,1), (0,-1)]}
                
            layoutLine.append(node)
            
        nodeLayout.append(layoutLine)
           
    return nodeLayout
            
# Function to shoot a beam from anywhere, given a layout
def shootBeam(layout, direction, pos):
    
    # Set of all energized tiles
    energized = set()
    
    # Set of explored tiles and directions
    explored = set()
    
    # Queue for exploring
    queue = [(pos, direction)]
    
    # While there are things left to explore
    while len(queue) > 0:
        
        # Pop the queue
        pos, direction = queue.pop()
    
        # Check if we should continue
        if (pos, direction) in explored:
            continue
        if pos[0] < 0 or pos[0] >= len(layout):
            continue
        if pos[1] < 0 or pos[1] >= len(layout[1]):
            continue
   
        # Add the node and direction to sets
        explored.add((pos, direction))
        energized.add(pos)
    
        # Find the node in the grid
        node = layout[pos[0]][pos[1]]
    
        # Find its next positions and add to queue
        if direction in node.directions:
            for d in node.directions[direction]:
                newPos = (pos[0] + d[0], pos[1] + d[1])
                queue.append((newPos, d))
        else:
            newPos = (pos[0] + direction[0], pos[1] + direction[1])
            queue.append((newPos, direction))
        
    return energized

# Read and parse the input
f = open('input.txt', 'r')
layout = f.read().split('\n')

# Parse into nodes
layout = parse(layout)

# Compute the results, when shooting beam from top left
energizedTopLeft = len(shootBeam(layout, (0,1), (0,0)))

# Find the max, by going through every possible starting point
energizedMax = -1
for i in range(len(layout)):
    
    energized = len(shootBeam(layout, (0, 1), (i, 0)))
    if energized > energizedMax:
        energizedMax = energized
    energized = len(shootBeam(layout, (0, -1), (i, len(layout[0])-1)))
    if energized > energizedMax:
        energizedMax = energized
for i in range(len(layout[0])):
    
    energized = len(shootBeam(layout, (1, 0), (0, i)))
    if energized > energizedMax:
        energizedMax = energized
    energized = len(shootBeam(layout, (-1, 0), (len(layout)-1, i)))
    if energized > energizedMax:
        energizedMax = energized

# Print the results
print(f'Shooting the beam from the top left corner, {energizedTopLeft} tiles are energized')
print(f'Shooting the beam from the optimal position, {energizedMax} become energized')