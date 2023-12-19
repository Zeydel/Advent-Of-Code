# Function to extract vertex coordinates from the plan
def get_vertex_coordinates(plan):
    
    # Start at origo
    pos = (0,0)
    
    # Initial coordinate is 0
    vertex_coordinates = [pos]
    
    # List of rections is empty
    directions = []
    
    # Map direction to coordinate
    dir_map = {'R': (0,1),
               'L': (0,-1),
               'U': (-1,0),
               'D': (1,0)}
    
    # For evry line
    for p in plan:
        
        # Extract direction and length
        d, l, _ = p.split()
        
        # Map direction and convert length to integer
        d_dir = dir_map[d]
        l = int(l)
        
        # Calculate new position
        d_dir = (d_dir[0] * l, d_dir[1] * l)
        pos = (pos[0] + d_dir[0], pos[1] + d_dir[1])
        
        # Add coordinate and direction
        vertex_coordinates.append(pos)
        directions.append(d)
        
    # Return coordinates and direction
    return vertex_coordinates, directions
       
# Function to extract vertex coordinates from the hex numbers in the plan 
def get_real_vertex_coordinaes(plan):
    
    # Init same as above
    pos = (0,0)
    vertex_coordinates = [pos]
    directions = []
    
    dir_map = {'R': (0,1),
               'L': (0,-1),
               'U': (-1,0),
               'D': (1,0)}
    
    # For every line
    for p in plan:
        
        # Extract the hex number
        _, _, h = p.split()
        
        # Find the firection
        d = h[-2]
        if d == '0':
            d = 'R'
        elif d == '1':
            d = 'D'
        elif d == '2':
            d = 'L'
        elif d == '3':
            d = 'U'
        
        # Convert hex number to decimal
        l = int(h[2:7], 16)
        
        # Then do the same as above
        d_dir = dir_map[d]
        l = int(l)

        d_dir = (d_dir[0] * l, d_dir[1] * l)
        pos = (pos[0] + d_dir[0], pos[1] + d_dir[1])
        
        vertex_coordinates.append(pos)
        directions.append(d)
            
    return vertex_coordinates, directions

# Function to offset coordinates to avoid off-by-one errors
def get_offset_coordinates(coordinates, directions):
    
    # If we find three directions in a row that go clockwise, we add, otherwise we subtract
    addDir = 'RDLURD'
    subtractDir = 'DRULDR'
    
    # Swap these if we are going counterclockwise
    if not is_clockwise(coordinates):
        addDir, subtractDir = subtractDir, addDir

    # Init offsets as zero
    x_offset = 0
    y_offset = 0
    
    # Init empty list of coordinates
    offset_coordinates = [(0,0)]
    
    # For every coordinate
    for i, c in enumerate(coordinates[:-1]):
        
        # Extract values, plus values of the next coordinates
        x1, y1 = c
        x2, y2 = coordinates[i+1]
        
        # Find the path
        path = directions[i-1] + directions[i % len(directions)] + directions[(i+1) % len(directions)]
        
        # If we have to add, add
        if path in addDir:
            if x2 > x1:
                x_offset += 1
            elif x2 < x1:
                x_offset -= 1
            elif y2 > y1:
                y_offset += 1
            else:
                y_offset -= 1
        # If we have to subtract, do so
        elif path in subtractDir:
            if x2 > x1:
                x_offset -= 1
            elif x2 < x1:
                x_offset += 1
            elif y2 > y1:
                y_offset -= 1
            else:
                y_offset += 1
            
        # Then add the offset coordinate
        offset_coordinates.append((x2+x_offset, y2+y_offset))
        
    return offset_coordinates
            
# Get area of the pool using the shoelace method
def get_pool_area(coordinates, directions):

    # Init area as zero
    area = 0
            
    # For every pair of coordinates
    for i, c in enumerate(coordinates[:-1]):
            
        x1, y1 = c
        x2, y2 = coordinates[i+1]
                    
        # Add this to total
        area += (x1*y2) - (x2*y1)
        
    # Take half of the absolute value
    area = abs(area)
    area //= 2
    
    return area
        
# Function to figure out whether we are going clockwise or counterclockwise
def is_clockwise(coordinates):
    
    edgeSum = 0
    
    for i, c in enumerate(coordinates[:-1]):
        
        edgeSum += (coordinates[i+1][0] - c[0]) * (coordinates[i+1][1] + c[1])
        
    # We this sum is positive, we are going clockwise
    return edgeSum > 0
    


# Read and parse the input
f = open('input.txt', 'r')
plan = f.read().split('\n')

# Compute the area of the small pool
vertex_coordinates, directions = get_vertex_coordinates(plan)
offset_coordinates = get_offset_coordinates(vertex_coordinates, directions)
area = get_pool_area(offset_coordinates, directions)

# Compute the area of the large pool
vertex_coordinates, directions = get_real_vertex_coordinaes(plan)
offset_coordinates = get_offset_coordinates(vertex_coordinates, directions)
big_area = get_pool_area(offset_coordinates, directions)

print(f'The area of the small pool is {area}')
print(f'The area of the big pool is {big_area}')
