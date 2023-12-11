# Class for a node
class Node:
    def __init__(self, x, y, shape):
        self.neighbors = []
        self.coordinates = (x,y)
        self.shape = shape
        
# Parse the text into a graph representing the main loop
def parse(pipeMap):
    
    explored = {}
    
    startNode = None
    
    # Create node for each space in the grid
    for x, line in enumerate(pipeMap):
        for y, c in enumerate(line):
            
            node = Node(x, y, c)
            
            neighbors = []
            
            # Find potential neighbors depending on shape. Also store which
            # symbols neighbors need in order to connect
            if c == '|':
                neighbors.append(((x-1, y), ('|', 'F', '7', 'S')))
                neighbors.append(((x+1, y), ('|', 'L', 'J', 'S')))
            elif c == '-':
                neighbors.append(((x, y-1), ('-', 'L', 'F', 'S')))
                neighbors.append(((x, y+1), ('-', 'J', '7', 'S')))
            elif c == 'L':
                neighbors.append(((x-1, y), ('|', 'F', '7', 'S')))
                neighbors.append(((x, y+1), ('-', 'J', '7', 'S')))
            elif c == 'J':
                neighbors.append(((x-1, y), ('|', 'F', '7', 'S')))
                neighbors.append(((x, y-1), ('-', 'L', 'F', 'S')))
            elif c == '7':
                neighbors.append(((x+1, y), ('|', 'L', 'J', 'S')))
                neighbors.append(((x, y-1), ('-', 'L', 'F', 'S')))
            elif c == 'F':
                neighbors.append(((x+1, y), ('|', 'L', 'J', 'S')))
                neighbors.append(((x, y+1), ('-', 'J', '7', 'S')))
            elif c == 'S':
                neighbors.append(((x-1, y), ('|', 'F', '7')))
                neighbors.append(((x+1, y), ('|', 'L', 'J')))
                neighbors.append(((x, y-1), ('-', 'L', 'F')))
                neighbors.append(((x, y+1), ('-', 'J', '7')))
                startNode = node
            
            # For every potential neighbor, check if symbol matches. Add to list if so
            for n in neighbors:
                if n[0] in explored and explored[n[0]].shape in n[1]:
                    node.neighbors.append(explored[n[0]])
                    explored[n[0]].neighbors.append(node)
                    
            # If we are at the starting node, figure out what shape it is
            if node.shape == 'S':
                neihborCoordinates = [n.coordinates for n in node.neighbors]
                
                if (x-1, y) in neihborCoordinates and (x+1, y) in neihborCoordinates:
                    node.shape = '|'
                elif (x, y-1) in neihborCoordinates and (x, y+1) in neihborCoordinates:
                    node.shape = '|'
                elif (x-1, y) in neihborCoordinates and (x, y+1) in neihborCoordinates:
                    node.shape = 'L'
                elif (x-1, y) in neihborCoordinates and (x, y-1) in neihborCoordinates:
                    node.shape = 'J'
                elif (x+1, y) in neihborCoordinates and (x, y-1) in neihborCoordinates:
                    node.shape = '7'
                elif (x+1, y) in neihborCoordinates and (x, y+1) in neihborCoordinates:
                    node.shape = 'F'
                                    
            explored[(x, y)] = node
     
    # Return the start node               
    return startNode

    
# Do a BFS to count number of nodes in loop
def get_bfs_depth_and_main_loop_coordinates(node):
    
    explored = set()
    queue = [(node, 0)]    
    maxDepth = -1
    
    while len(queue) > 0:
        cur, depth = queue.pop(0)
        
        if depth > maxDepth:
            maxDepth = depth
        
        for n in cur.neighbors:
            if n.coordinates not in explored:
                queue.append((n, depth + 1))
                
        explored.add(cur.coordinates)
        
    # Return max depth discovered and the set of coordinates in the loop
    return maxDepth, explored

# Count all nodes contained in the loop
def count_nodes_in_loop(pipeMap, coordinates, startingNode):
    
    count = 0
    
    # For every line
    for x, line in enumerate(pipeMap):
        
        inside = False
        edge = ''
        
        # For every character
        for y, c in enumerate(line):
            
            # For the starting node, use the computed shape
            if c == 'S':
                c = startingNode.shape
            
            # If we are inside the loop, add 1
            if (x, y) not in coordinates and inside:
                count += 1
                
            # If we have found a |, flip the inside var
            elif c == '|' and (x, y) in coordinates:
                inside = not inside
                
            # Edge detection
            elif c == 'F' and (x, y) in coordinates:
                edge = 'F'
            elif c == 'J' and edge == 'F':
                inside = not inside
                edge = ''
            elif c == '7' and edge == 'F':
                edge = ''
            elif c == 'L' and (x, y) in coordinates:
                edge = 'L'
            elif c == '7' and edge == 'L':
                inside = not inside
                edge = ''
            elif c == 'J' and edge == 'L':
                edge = ''
        
    return count
        

# Read and parse the input
f = open('input.txt', 'r')
pipeMap = f.read().split('\n')

# Parse and calculate
startingNode = parse(pipeMap)
bfs_depth, main_loop_coordinates = get_bfs_depth_and_main_loop_coordinates(startingNode)

# Print the results
print(f'The furthers node is {bfs_depth} away')
print(f'{count_nodes_in_loop(pipeMap, main_loop_coordinates, startingNode)} nodes are contained within the loop')
