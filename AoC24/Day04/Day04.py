# Init direction to search for the string XMAS
def init_xmas_search_directions():
    
    # Start with empty list
    directions = []
    
    # Add every direction to list
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            directions.append((dx, dy))
            
    # Return list
    return directions

# Init list of pairs of directions that create an X
def init_x_mas_search_directions():
    
    return [((-1, -1), (-1, 1)),
            ((-1, 1), (1, 1)),
            ((1, 1), (1, -1)),
            ((1, -1), (-1, -1))]

# Search for the word XMAS in lines along all defined directions from a starting point
def search_xmas(lines, x, y, search_directions):
    
    # If it doesn't start at an X, we are never going to be able to spell XMAS
    if lines[y][x] != 'X':
        return 0
    
    # Init count as zero
    xmas_count = 0
    
    # For every direction
    for dx, dy in search_directions:
        
        # Create empty string
        string = ''
        
        # Add the letters along the direction to the string
        for i in range(4):
            
            nx = x + (i*dx)
            ny = y + (i*dy)
            
            # Break if we go out of bounds
            if ny < 0 or ny >= len(lines):
                break
            
            if nx < 0 or nx >= len(lines[y]):
                break
           
            string += lines[ny][nx]
            
        # If the string equals XMAS, add one to count
        if string == 'XMAS':
            xmas_count += 1
            
    # Return count
    return xmas_count

# Search lines for X of MAS strings
def search_x_mas(lines, x, y, search_directions):
    
    # If we are not at an A, return 0
    if lines[y][x] != 'A':
        return 0
    
    # If we are on the edge, return 0
    if y == 0 or x == 0:
        return 0
    
    if y == len(lines)-1 or x == len(lines[y])-1:
        return 0
    
    # Init count
    x_mas_count = 0
    
    # For every pair of directions that create an X
    for d1, d2 in search_directions:
        
        nx1 = x + d1[0]
        ny1 = y + d1[1]
        
        nx2 = x + d2[0]
        ny2 = y + d2[1]
        
        # Check if there is an M on both directions
        if lines[ny1][nx1] != 'M' or lines[ny2][nx2] != 'M':
            continue
        
        nx1 = x - d1[0]
        ny1 = y - d1[1]
        
        nx2 = x - d2[0]
        ny2 = y - d2[1]   
    
        # Check that there is an S on the opposite side of both M
        if lines[ny1][nx1] != 'S' or lines[ny2][nx2] != 'S':
            continue
        
        # Increase count
        x_mas_count += 1
        
    # Return count
    return x_mas_count

# Open file and read lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Init search directions
xmas_search_directions = init_xmas_search_directions()
x_mas_search_directions = init_x_mas_search_directions()

# Init counts
total_xmas_count = 0
total_x_mas_count = 0

# Search for words
for y in range(len(lines)):
    for x in range(len(lines[y])):
        total_xmas_count += search_xmas(lines, x, y, xmas_search_directions)
        total_x_mas_count += search_x_mas(lines, x, y, x_mas_search_directions)
        
# Print the result
print(f'{total_xmas_count} is the number of XMASes in the word search')
print(f'{total_x_mas_count} is the number of MAS Xes in the grid')