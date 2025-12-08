# Parse input into a start position along with sets of empty space and splitters
def parse(lines):
    
    start = (-1, -1)
    
    space = set()
    splitters = set()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char == 'S':
                start = (x, y)
            elif char == '.':
                space.add((x, y))
            elif char == '^':
                splitters.add((x, y))
                
    return start, space, splitters

# Use BFS to count how many times the beam splits
def get_split_count(start, space, splitters):
    
    # Init answer as zero
    splits = 0
    
    # Make a queue
    queue = [start]
    
    # Make a set of explored nodes
    explored = set()
    
    # While there are elements left in the queue
    while len(queue) > 0:
        
        # Pop the next element in the queue
        x, y = queue.pop(0)
        
        # Continue if we have already explored
        if (x, y) in explored:
            continue
        
        explored.add((x, y))
        
        # If we are at empty space, add the next spot down to the queue
        if (x, y) in space or (x, y) == start:
            queue.append((x, y+1))
            
        # If we are at a splitter, add the two sides to the queue and
        # increment splits
        elif (x, y) in splitters:
            splits += 1
            queue.append((x-1, y))
            queue.append((x+1, y))
            
    # Return the number of splits
    return splits

# Reursive method with memoization to get the total number of timelines
def get_timelines(start, space, splitters, memo_dict = dict()):
    
    # If we already know the answer, return it
    if start in memo_dict:
        return memo_dict[start]
    
    # Get the x and y values
    nx, ny = start
    
    # While we are at a knowns space
    while (nx, ny) in space or (nx, ny) in splitters or (nx, ny) == start:
        
        # If we reach a splitter
        if (nx, ny) in splitters:
            
            # Get the sum of timelines of going left and right
            left_timelines = get_timelines((nx-1, ny), space, splitters, memo_dict)
            right_timelines = get_timelines((nx+1, ny), space, splitters, memo_dict)
 
            # Save it in our dict and return it
            memo_dict[start] = left_timelines + right_timelines
 
            return memo_dict[start]
        
        # Go down one
        ny += 1
    
    # If we go outside the map, there is only one timeline. Save that and return 1
    memo_dict[start] = 1
    return memo_dict[start]

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
start, space, splitters = parse(lines)

# Compute the results
splits = get_split_count(start, space, splitters)
timelines = get_timelines(start, space, splitters)

print(f'The beam splits {splits} times')
print(f'There are {timelines} different timelines')