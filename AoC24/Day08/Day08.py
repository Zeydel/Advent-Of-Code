# Parse the input into a a dictionary of antenna characters with list of location as keys
def parse(lines):
    
    antenna_locations = dict()
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char == '.':
                continue
            
            if char not in antenna_locations:
                antenna_locations[char] = []
                
            antenna_locations[char].append((x,y))
            
    return antenna_locations, len(lines[0]), len(lines)

# Given a list of antenna locations and map bounds, return the set of antinode locations
def get_antinodes(antenna_locations, max_x, max_y):
    
    # Init empty set
    antinodes = set()
    
    # For evry pair of antenna locations
    for loc_1_x, loc_1_y in antenna_locations:
        for loc_2_x, loc_2_y in antenna_locations:
            
            # If both locations are the same, return
            if loc_1_x == loc_2_x and loc_1_y == loc_2_y:
                continue
            
            # Calculate the difference
            x_dif = loc_1_x - loc_2_x
            y_dif = loc_1_y - loc_2_y
            
            # Add the difference to the first location
            x_loc = loc_1_x + x_dif
            y_loc = loc_1_y + y_dif
            
            # If we are within bounds, add the location to the result set
            if is_in_bounds(x_loc, y_loc, max_x, max_y): 
                antinodes.add((x_loc, y_loc))
            
    # Return the set
    return antinodes
            
# Similar to the function aboce, but finds every antinode on the path
def get_antinodes_line(antenna_locations, max_x, max_y):
    
    antinodes = set()
    
    for loc_1_x, loc_1_y in antenna_locations:
        for loc_2_x, loc_2_y in antenna_locations:
            if loc_1_x == loc_2_x and loc_1_y == loc_2_y:
                continue
            
            # Add both antenna locations to the set
            antinodes.add((loc_1_x, loc_1_y))
            antinodes.add((loc_2_x, loc_2_y))
            
            x_dif = loc_1_x - loc_2_x
            y_dif = loc_1_y - loc_2_y
            
            x_loc = loc_1_x + x_dif
            y_loc = loc_1_y + y_dif
            
            # While we are in bounds, add the result to the first location 
            # and add again
            while is_in_bounds(x_loc, y_loc, max_x, max_y):
                antinodes.add((x_loc, y_loc))
                
                x_loc += x_dif
                y_loc += y_dif
            
    return antinodes

# Helper function to find out if we are in map bounds
def is_in_bounds(x_loc, y_loc, max_x, max_y):
    
    if x_loc < 0 or x_loc >= max_x:
        return False
    if y_loc < 0 or y_loc >= max_y:
        return False
    return True

# Open file and read lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
antenna_locations, max_x, max_y = parse(lines)

# Init sets
antinodes = set()
antinodes_line = set()

# For every list of locations
for char in antenna_locations:
    
    # Get the antinodes using both methods and add to their sets
    antinodes |= get_antinodes(antenna_locations[char], max_x, max_y)
    antinodes_line |= get_antinodes_line(antenna_locations[char], max_x, max_y)
    
# Print the results
print(f'{len(antinodes)} antinodes are present')
print(f'{len(antinodes_line)} antonodes are present using the updated model')