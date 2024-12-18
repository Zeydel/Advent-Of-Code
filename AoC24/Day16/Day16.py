# Im not gonna make my own heap
from heapq import heappush, heappop

# Parse the input into points on path, start, and end position
def parse(lines):
    
    path = set()
    start = (-1, -1)
    end = (-1, -1)
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char != '#':
                path.add((x,y))
                
            if char == 'S':
                start = (x, y)
                
            if char == 'E':
                end = (x,y)
                
    return path, start, end

# Get every direction we can travel in
def get_directions():
    
    return [(1,  0), # east
            (-1, 0), # west
            (0,  1), # north
            (0, -1)] # south

# Init the vars used for dijkstra
def init_queue(path):
    
    queue = set()
    dists = dict()
    pred = dict()
    
    directions = get_directions()
    
    for pos in path:
        for direction in directions:
            
            queue.add((pos, direction))
            dists[(pos, direction)] = float('inf')
            pred[(pos, direction)] = []
            
    return queue, dists, pred
        
# Funky version of dijkstra
def get_shortest_paths(path, start):
    
    # Get the variables for each vertex
    queue, dists, pred = init_queue(path)
    
    # Init a heap
    heap = []
    
    # Add the starting node and starting direction to
    # the heap
    heappush(heap, (0, (start, (1,0))))
    
    # Get the direction we can travel in
    directions = get_directions()
    
    # While there are more nodes left to explore
    while len(queue) > 0:
                
        # Find the element in queue that has the highest
        # priority
        value = -1
        
        while value not in queue:
        
            dist, value = heappop(heap)
        
        # Remove it from queue and unpack the values
        queue.remove(value)
        pos, direction = value
        
        # For every direction we can turn, that is not the same as the initial or 180 degrees away
        for new_dir in directions:
            if new_dir == direction or (new_dir[0] == direction[0] * -1 and new_dir[1] == direction[1] * -1):
                continue
            
            # If we have explored it, continue
            if (pos, new_dir) not in queue:
                continue
                            
            # If it is better than the distance we have so far
            if dist + 1000 < dists[(pos, new_dir)]:
                
                # Remember the new distance
                dists[(pos, new_dir)] = dist + 1000
                
                # Set the current vertex as a predecessor
                pred[(pos, new_dir)] = [value]
                
                # Add the new position to the heap
                heappush(heap, (dist+1000, (pos, new_dir)))
                    
            # If it is as good as a previous result, add current
            # vertex to predecessor list
            elif dist + 1000 == dists[(pos, new_dir)]:
                pred[(pos, new_dir)].append(value)
        
        # Unpack some vars to make it more readable
        px, py = pos
        dx, dy = direction
        
        # If going forward one step would go out of the path, continue
        if (px + dx, py + dy) not in path:
            continue
            
        # If we have alreade explored the space, continue
        if ((px + dx, py + dy), direction) not in queue:
            continue
        
        # Same as above, just hoing forward instead of turning
        if dist + 1 < dists[((px + dx, py + dy), direction)]:
            dists[((px + dx, py + dy), direction)] = dist + 1
            pred[((px + dx, py + dy), direction)] = [value]
            
            heappush(heap, (dist+1, ((px + dx, py + dy), direction)))
                
        elif dist + 1 == dists[((px + dx, py + dy), direction)]:
            pred[((px + dx, py + dy), direction)].append(value)
            
    return dists, pred
    
# Gets the minimum distance to a point
def get_min_dist_to_point(dists, end):
    
    min_dist = float('inf')
    best_dirs = []
        
    # Go trough every direction and get the minimum distance
    for direction in get_directions():
        
        if dists[(end, direction)] < min_dist:
            min_dist = dists[(end, direction)]
            best_dirs = [direction]
            
        elif dists[(end, direction)] == min_dist:
            best_dirs.append(direction)
    
    return min_dist, best_dirs

# Get the number of points that lie of a best path
def get_points_on_best_paths(end, pred, best_dirs):
    
    points = set()
        
    points.add(end)
    
    queue = []
    
    for direction in best_dirs:
        queue.append((end, direction))
    
    while len(queue) > 0:
        
        pos, direction = queue.pop()
        
        points.add(pos)
                
        for prev in pred[(pos, direction)]:
            queue.append(prev)
            
    return len(points)
         
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
path, start, end = parse(lines)

# Gerform all points shortest path
dists, pred = get_shortest_paths(path, start)

# Get min distance
min_dist, best_dirs = get_min_dist_to_point(dists, end)

# Get the number of points that lie on the min distance
num_points = get_points_on_best_paths(end, pred, best_dirs)

# Print the results
print(f'{min_dist} is the minimum distance')
print(f'{num_points} is the number of tiles on best paths')