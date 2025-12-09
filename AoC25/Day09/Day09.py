from heapq import heappush, heappop

# Parse the input into a list of coordinates. Double the integers to 
# avoid some edgecases in part 2
def parse(lines):
    
    coordinates = []
    
    for line in lines:
        x, y = line.split(',')
        
        coordinates.append((int(x) * 2, int(y) * 2))
        
    return coordinates

# Get the size of the rectange. Calculation is changed because the coordinates
# are doubled
def get_rectange_size(c1, c2):
    
    width = abs(c1[0] - c2[0]) + 2
    height = abs(c1[1] - c2[1]) + 2
    
    return height * width

# Get the sizes of all rectanged sorted by biggest to largets
def get_rectangle_sizes(coordinates):
    
    sizes = []
    
    for i, c1 in enumerate(coordinates):
        for c2 in coordinates[i+1:]:
            
            size = get_rectange_size(c1, c2)
            
            heappush(sizes, (-size, c1, c2))
                
    return sizes
    
# Get all nodes that lay in the boundry of the shape
def get_boundry_nodes(coordinates):
    
    boundry = set()
    
    for i in range(len(coordinates)):
        
        c1x, c1y = coordinates[i]
        c2x, c2y = coordinates[(i+1) % len(coordinates)]
        
        if c1x == c2x:
            boundry |= {(c1x, y) for y in range(min(c1y, c2y), max(c1y, c2y)+1)}
        else:
            boundry |= {(x, c1y) for x in range(min(c1x, c2x), max(c1x, c2x)+1)}
            
    return boundry

# Get the neighbors of a single node
def get_neighbors(x, y):
    
    neighbours = set()
    
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            
            if nx == x and ny == y:
                continue
            
            neighbours.add((nx, ny))
            
    return neighbours

# Get all nodes that are just outside the boundry of the shape
def get_outer_boundry(coordinates):
    
    # Start by getting the boundry
    boundry = get_boundry_nodes(coordinates)
    
    # Find min and max values for x and y
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')
    
    for x, y in coordinates:
        
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        
        min_y = min(y, min_y)
        max_y = max(y, max_y)
        
    # Extend the perimeter by one
    min_x -= 1
    min_y -= 1
    
    max_x += 1
    max_y += 1
    
    # Find the middle of the y axis
    middle_y = (min_y + max_y) // 2
    
    # Define a point
    outer_boundry_point = (min_x, middle_y)
    
    # Go right until we are next to a boundry point
    while (outer_boundry_point[0] + 1, middle_y) not in boundry:
        
        outer_boundry_point = (outer_boundry_point[0] + 1, middle_y)
        
    # Make a queue
    queue = [outer_boundry_point]
    
    # Define an outer boundry
    outer_boundry = set()
    
    # Define a set of explored notes
    explored = set()
    
    # Do a search around the boundry
    while len(queue) > 0:
        
        # Take the next element
        x, y = queue.pop()
        
        # If we have seen it, continue
        if (x, y) in explored:
            continue
        
        explored.add((x, y))
        
        # Get the neighbours
        neighbors = get_neighbors(x, y)
        
        # If it is next to the boundry, but not part of it, add it to the set
        if len(boundry & neighbors) > 0 and (x, y) not in boundry:
            outer_boundry.add((x, y))
            
        # Otherwise continue
        else:
            continue
            
        # Add every neighbor to queue
        for n in neighbors:
            queue.append(n)
        
    # Return the outer boundry
    return outer_boundry
        
# Check if the rectangle defined by two points are within the boundry
# of the shape
def is_rectange_in_tiles(c1, c2, outer_boundry):
    
    # Get max and min values for x and y
    c1x, c1y = c1
    c2x, c2y = c2
    
    min_x = min(c1x, c2x)
    max_x = max(c1x, c2x)
    
    min_y = min(c1y, c2y)
    max_y = max(c1y, c2y)
        
    # For every coordinate on the rectangle boundry, check if a point
    # is on the outside bounds of the big shape. If so return False
    for x in [min_x, max_x]:
        for y in range(min_y, max_y+1):
            if (x, y) in outer_boundry:
                return False
    
    for y in [min_y, max_y]:
        for x in range(min_x, max_x+1):
            if (x, y) in outer_boundry:
                return False

    # Return True, if we couldn't find any points outside the shape
    return True

# Get the biggest rectangle
def get_biggest_rectange(coordinates, sizes):
    
    # Get the outer boundry
    boundry = get_outer_boundry(coordinates)
    
    # Search every pair of coordinates
    while True:
        
        # Pop the next biggest shape
        cur_size, c1, c2 = heappop(sizes)
                
        # If it is contained within the rectangle, return its size
        if is_rectange_in_tiles(c1, c2, boundry):
            return -cur_size
        
    return -1
    

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
coordinates = parse(lines)

# Get sizes of the rectangles defined by all pairs of coordinates
sizes = get_rectangle_sizes(coordinates)

# Get the biggest rectange
biggest_rectange = -sizes[0][0] // 4

# Get the biggest rectangle that is within the shape
biggest_rectange_in_tiles = get_biggest_rectange(coordinates, sizes) // 4

# Print the results
print(f'The biggest rectangle that can be made by two points has an area of {biggest_rectange}')
print(f'The biggest rectangle that can be made only of tiles has an area of {biggest_rectange_in_tiles}')