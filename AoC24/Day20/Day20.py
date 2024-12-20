# Parse input into list of points on path, start and end
def parse(lines):
    
    points = set()
    start = (-1, -1)
    end = (-1, -1)
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char != '#':
                points.add((x, y))
                
            if char == 'S':
                start = (x, y)
                
            if char == 'E':
                end = (x, y)

    return points, start, end

# Get cardinat directions
def get_directions():
    
    return [(1,  0),
            (-1, 0),
            (0,  1),
            (0, -1)]

# Get the distance from all points to end by BFS
def get_all_dists_to_end(points, end):
    
    dists = dict()
    
    directions = get_directions()
    
    explored = set()
    explored.add(end)
    
    queue = []
    queue.append((0, (end)))
    
    while len(queue) > 0:
        
        dist, point = queue.pop(0)
    
        dists[point] = dist    
    
        px, py = point
    
        for dx, dy in directions:
            
            nx, ny = px + dx, py + dy
            
            if (nx, ny) in explored:
                continue
            
            if (nx, ny) not in points:
                continue
            
            queue.append((dist + 1, (nx, ny)))
            explored.add((nx, ny))
            
    return dists
            
# Get the cheat distances for a single point
def get_cheat_dist(cheat_start, dists, cheat_limit):
    
    # Init a dict to store cheat distances
    cheat_dists = dict()
    
    # And normal BFS stuff
    directions = get_directions()
    
    explored = set()
    explored.add(cheat_start)
    
    queue = []
    queue.append((0, cheat_start))
    
    cheat_start_dist = dists[cheat_start]
    
    while len(queue) > 0:
        
        dist, point = queue.pop(0)
        
        px, py = point
    
        # If we are at a valid point
        if (px, py) in points:
            
            # Find out how much we gain from going there by cheating
            cheat_gain = (cheat_start_dist - dists[(px, py)]) - dist
            
            # If it is positive, add it to dic
            if cheat_gain > 0:
            
                if cheat_gain not in cheat_dists:
                    cheat_dists[cheat_gain] = 0
                
                cheat_dists[cheat_gain] += 1
        
        # If we are at the cheating limit, stop the search
        if dist == cheat_limit:
            continue
        
        # Normal BFS stuff
        for dx, dy in directions:
            
            nx, ny = px + dx, py + dy
            
            if (nx, ny) in explored:
                continue
            
            queue.append((dist + 1, (nx, ny)))
            explored.add((nx, ny))
            
    return cheat_dists
    
# Run the cheat search for all points
def get_all_cheat_dists(dists, cheat_limit):

    # Return a dict containing number of cheats for each distance
    cheat_dist_dict = dict()    

    for point in dists:
        
        cheat_dists = get_cheat_dist(point, dists, cheat_limit)
        
        for cheat_dist in cheat_dists:
                        
            if cheat_dist not in cheat_dist_dict:
                cheat_dist_dict[cheat_dist] = 0
                
            cheat_dist_dict[cheat_dist] += cheat_dists[cheat_dist]
            
    return cheat_dist_dict

# Read input as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse input
points, start, end = parse(lines)

# Get all distances to end
dists = get_all_dists_to_end(points, end)

# Get cheats with a cheat distance of 2
cheat_dists = get_all_cheat_dists(dists, 2)

# Count cheats that save more than 100 picoseconds
cheats_over_100_2_seconds = 0

for cheat_dist in cheat_dists:
    
    if cheat_dist >= 100:
        cheats_over_100_2_seconds += cheat_dists[cheat_dist]
        
# Do the same thing again, but for 20 seconds
cheat_dists = get_all_cheat_dists(dists, 20)

cheats_over_100_20_seconds = 0

for cheat_dist in cheat_dists:
    
    if cheat_dist >= 100:
        cheats_over_100_20_seconds += cheat_dists[cheat_dist]
        
        
print(f'{cheats_over_100_2_seconds} is the number of cheats over 100 picoseconds, when cheating for 2 picosends')
print(f'{cheats_over_100_20_seconds} is the number of cheats over 100 picoseconds, when cheating for 20 picosends')