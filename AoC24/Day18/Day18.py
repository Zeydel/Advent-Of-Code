# Parse the input into a list of points
def parse(lines):
    
    points = []
    
    for line in lines:
        
        split_line = line.split(',')
        
        points.append((int(split_line[0]), int(split_line[1])))

    return points

# Get the directions we can move along
def get_directions():
    
    return [(1,  0),
            (-1, 0),
            (0,  1),
            (0, -1)]

# Tell if a point is within the boundry
def is_in_bounds(point, end):
    
    max_x, max_y = end
    x, y = point
    
    if y < 0 or y > max_y:
        return False
    
    if x < 0 or x > max_x:
        return False
    
    return True

# Get the length of the shortest path
def get_shortest_path(start, end, points, memory_limit = -1):
    
    # If we have a memory limit, remove all the bytes from outside the limit
    if memory_limit != -1:
        points = points[:memory_limit]
        
    # Convert set to point
    points = set(points)
        
    # Create BFS stuff
    queue = []
    queue.append((0, start))
    
    directions = get_directions()
    
    explored = set()
    explored.add(start)
    
    # Do BGS
    while len(queue) > 0:
        
        dist, point = queue.pop(0)
        px, py = point
        
        # If we have found the end, return its distance
        if (px, py) == end:
            return dist
        
        for dx, dy in directions:
            
            nx, ny = px + dx, py + dy
            
            if (nx, ny) in explored:
                continue
            
            if not is_in_bounds((nx, ny), end):
                continue
            
            if (nx, ny) in points:
                continue
            
            queue.append((dist + 1, (nx, ny)))
            explored.add((nx, ny))
            
    return float('inf')
        
# Get the first byte the prevents exit
def get_first_byte_that_prevents_exit(start, end, points):
    
    for i, point in enumerate(points):
        
        if get_shortest_path(start, end, points, i+1) == float('inf'):
            return point
        
    return (-1, -1)
    

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the lines into points
points = parse(lines)

# Init problem vars
start = (0,0)
end = (70,70)

memory_limit = 1024

# Get the lenth of the shortest path
shortest_path = get_shortest_path(start, end, points, memory_limit)
byte_that_prevents_exit = get_first_byte_that_prevents_exit(start, end, points)

# Print the results
print(f'{shortest_path} is the length of the shortest path')
print(f'{byte_that_prevents_exit[0]},{byte_that_prevents_exit[1]} is the first byte that prevents exit')