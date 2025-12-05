# Parse input into a set of coordinates for all rolls
def parse(lines):
    
    rolls = set()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char == '@':
                rolls.add((x, y))
                
    return rolls

# Get the neighbors for a given x and y coordinate
def get_neighbors(x, y):
    
    neighbors = set()
    
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            
            if nx == x and ny == y:
                continue
            
            neighbors.add((nx, ny))
            
    return neighbors

# Get rolls accessible for removal
def get_acessible_rolls(rolls):
    
    # Init as zero
    accessible_rolls = 0
    
    # For every rolls coordinate
    for x, y in rolls:
                
        # Get neighbor coordinate
        neighbors = get_neighbors(x, y)
        
        # If fewer than 4 of the neighbors are rolls, increment counter
        if len(rolls & neighbors) < 4:
            accessible_rolls += 1
    
    # Return the accessible rolls
    return accessible_rolls

# Get rolls accessible for removal, considering that some rolls are
# being removed underway
def get_acessible_rolls_with_removals(rolls):
    
    # Start by counting neighbors for each roll
    neighbor_counts = dict()
    
    for x, y in rolls:
        
        neighbor_counts[(x, y)] = len(rolls & get_neighbors(x, y))
        
    # Init a queue of all rolls
    queue = {roll for roll in rolls}
    
    # Set of rolls that can be removed
    removed = set()
    
    # While there is something left in the queue
    while len(queue) > 0:
        
        # Pop next element
        x, y = queue.pop()
        
        # If the roll has already been removed, continue
        if (x, y) in removed:
            continue
        
        # If the neighbor count is less than 4, add to set of removed rolls
        if neighbor_counts[(x, y)] < 4:
            removed.add((x,y))
            
            # For every neighbor that is a roll
            for nx, ny in (get_neighbors(x, y) & rolls):
                
                # Add to queue and decrement its neighbor count
                queue.add((nx, ny))
                neighbor_counts[(nx, ny)] -= 1
                
    # Return the lenght of removed rolls
    return len(removed)
            
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
rolls = parse(lines)

# Calculate results
accessible_rolls = get_acessible_rolls(rolls)
accessible_rolls_with_removals = get_acessible_rolls_with_removals(rolls)

# Print the results
print(f'{accessible_rolls} rolls can be removed initially')
print(f'{accessible_rolls_with_removals} can be removed in total')