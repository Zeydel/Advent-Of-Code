# Get the position of every trailhead in the map
def get_trailheads(lines):
    
    trailheads = set()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char == '0':
                trailheads.add((x,y))
                
    return trailheads
   
# Determine if a position is within bounds
def is_in_bounds(x, y, lines):
    
    if y < 0 or y >= len(lines):
        return False
    if x < 0 or x >= len(lines[y]):
        return False
    return True
   
# Get the score of a trailhead
def get_trailheads_score(pos, lines):

    # Init directions we can move in
    dirs = [(0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)]    

    # Init scpre
    score = 0    

    # Init a queue and a set of explred positions
    queue = []
    explored = set()
    explored.add(pos)
    
    # Add our starting position to queue, with height 0
    queue.append((pos[0], pos[1], 0))
    
    # While there is stuff left to explore
    while len(queue) > 0:
        
        # Pop the next value
        vx, vy, vn = queue.pop(0)
        
        # If we are at a peak, increment score and continue
        if vn == 9:
            score += 1
            continue
        
        # For every neightbor
        for direction in dirs:
            
            # Get the position
            dx = vx + direction[0]
            dy = vy + direction[1]
            
            # If we are out of bounds, continue
            if not is_in_bounds(dx, dy, lines):
                continue
            
            # Else if neightbour is one step higher and not explored, add it to
            # queue and explored set
            if int(lines[dy][dx]) == vn + 1 and (dx, dy) not in explored:
                queue.append((dx, dy, vn + 1))
                explored.add((dx, dy))
                
    # Return the score
    return score
        
# The same as above with one difference
def get_trailheads_rating(pos, lines):

    dirs = [(0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)]    

    rating = 0    

    queue = []
    explored = set()
    explored.add(pos)
    
    queue.append((pos[0], pos[1], 0))
    
    while len(queue) > 0:
        vx, vy, vn = queue.pop(0)
        
        if vn == 9:
            rating += 1
            continue
        
        for direction in dirs:
            
            dx = vx + direction[0]
            dy = vy + direction[1]
            
            # The check to see if the position is already in explored set
            # is removed to get every path to the peak
            if not is_in_bounds(dx, dy, lines):
                continue
            
            if int(lines[dy][dx]) == vn + 1:
                queue.append((dx, dy, vn + 1))
                explored.add((dx, dy))
                
            
    return rating
        
        
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Get every trailhead
trailheads = get_trailheads(lines)

# Init score and reating
total_score = 0
total_rating = 0

# For every trailhead, get the score and the rating
for trailhead in trailheads:
    total_score += get_trailheads_score(trailhead, lines)
    total_rating += get_trailheads_rating(trailhead, lines)
    
# Print the results
print(f'{total_score} is the total score')
print(f'{total_rating} is the total rating')