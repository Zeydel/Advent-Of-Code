# Init the numpad
def init_numpad():
    
    return [['7','8','9'],
            ['4','5','6'],
            ['1','2','3'],
            ['', '0','A']]

# Init the directional pad
def init_directional_pad():
    
    return [['', '^', 'A'],
            ['<', 'v', '>']]
  
# Init directions
def init_directions():

    return [(1, 0, '>'),
            (-1,0, '<'),
            (0, 1, 'v'),
            (0,-1, '^')]    

# Check if coordinate is within bounds of a keypad
def is_in_bounds(x, y, keypad):
    
    if y < 0 or y >= len(keypad):
        return False
    if x < 0 or x >= len(keypad[y]):
        return False
    if keypad[y][x] == '':
        return False
    return True
    
# Get every shortest path between two points of a keypad
def get_shortest_paths(start, end, keypad):
    
    start_pos = (-1, -1)
    end_pos = (-1, -1)
    
    for y, line in enumerate(keypad):
        for x, char in enumerate(line):
            if char == start:
                start_pos = (x, y)
                
            if char == end:
                end_pos = (x,y)
                
    queue = []
    queue.append(('', start_pos))
    
    directions = init_directions()
    
    paths = []
    
    while len(queue) > 0:
        
        path, pos = queue.pop(0)
        
        if pos == end_pos:
            paths.append(path)
            
        if len(paths) > 0 and len(path) > len(paths[0]):
            return paths
            
        px, py = pos
        
        for dx, dy, arrow in directions:
            
            nx = px + dx
            ny = py + dy
        
            if not is_in_bounds(nx, ny, keypad):
                continue
            
            queue.append((path + arrow, (nx, ny)))

# Get all shortest paths between two keys on keypads
def get_all_shortest_paths():
    
    shortest_paths = dict()
    
    numpad = init_numpad()
    
    keys = [key for keylist in numpad for key in keylist]
    
    for key1 in keys:
        for key2 in keys:
            if key1 == key2:
                continue
            
            if key1 == '' or key2 == '':
                continue
            
            shortest_paths[(key1, key2)] = get_shortest_paths(key1, key2, numpad)
                
    directional_path = init_directional_pad()
    
    keys = [key for keylist in directional_path for key in keylist]
    
    for key1 in keys:
        for key2 in keys:
            if key1 == key2:
                continue
            
            if key1 == '' or key2 == '':
                continue
            
            shortest_paths[(key1, key2)] = get_shortest_paths(key1, key2, directional_path)
    
    return shortest_paths
        
# Super smart method for getting shortest sequence of buttons for a given sequence
def get_shortest_input_length(shortest_paths, sequence, depth, cache_dict):
    
    # If we dont wanna recurse further, return the length of the sequence
    if depth == 0:
        return len(sequence)
            
    # Var for the shortest input length
    shortest_input_length = 0        
    
    # We want to start at A
    sequence = 'A' + sequence

    # If we already know the answer, return it
    if (sequence, depth) in cache_dict:
        return cache_dict[(sequence, depth)]
    
    # For every pair of keys in the sequence
    for i in range(len(sequence) - 1):
        
        key1, key2 = sequence[i], sequence[i+1]
        
        # If the keys are the same, we simply press the A button,
        # increment the input length
        if key1 == key2:
            shortest_input_length += 1
            continue
        
        # Init var for shortest path length
        shortest_path_length = float('inf')
        
        # Try every path between the two keys
        for path in shortest_paths[(key1, key2)]:
            
            # Get the path length
            path_length = get_shortest_input_length(shortest_paths, path + 'A', depth-1, cache_dict)
            
            # If it is better than the one we already have, store it
            if path_length < shortest_path_length:
                shortest_path_length = path_length
                
        # Add to length
        shortest_input_length += shortest_path_length
        
    # Cache the result
    cache_dict[(sequence, depth)] = shortest_input_length
        
    return shortest_input_length
            
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Get all shortest paths
shortest_paths = get_all_shortest_paths()

# Init result vars
complexity_sum_3_depth = 0
complexity_sum_25_depth = 0

# Init a cache dict 
cache_dict = dict()

# For every password
for password in lines:

    # Get the shortest sequence length for 3 and 25 robots
    shortest_password_input_3_depth = get_shortest_input_length(shortest_paths, password, 3, cache_dict)
    shortest_password_input_25_depth = get_shortest_input_length(shortest_paths, password, 26, cache_dict)
    
    # Get the numerical part
    numerical_part = int(password[0:3])

    # Add results to numbers
    complexity_sum_3_depth += shortest_password_input_3_depth * numerical_part
    complexity_sum_25_depth += shortest_password_input_25_depth * numerical_part
    
# Print the results
print(f'{complexity_sum_3_depth} is the lowest number of button presses with 2 robots')
print(f'{complexity_sum_25_depth} is the lowest number of button presses with 25 robots')