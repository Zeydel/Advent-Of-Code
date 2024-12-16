# Check if a coordinate is within the bounds of the map
def is_in_bounds(x, y, lines):
    
    if y < 0 or y >= len(lines):
        return False
    if x < 0 or x >= len(lines[y]):
        return False
    return True

# Get the set of points in an area
def get_area(x, y, lines):
    
    # The directions of adjecency that define an area
    dirs = [(1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]
    
    # The character at the point
    char = lines[y][x]
    
    # Sets to keep track of points and the area and explored points
    area = set()
    explored = set()
    
    # Init a queue
    queue = [(x, y)]
    
    # Whilere there is more left to explored
    while len(queue) > 0:
        
        # Pop the next element and add to area
        x, y = queue.pop()
        
        area.add((x, y))
        
        # For every direction we can go
        for direction in dirs:
            
            # Get the position
            dx = x + direction[0]
            dy = y + direction[1]
            
            # If we havent explored it yet
            if (dx, dy) not in explored:
                
                explored.add((dx, dy))
                
                # Check if it is in bounds, and that is it the correct character
                # then add to queue
                if is_in_bounds(dx, dy, lines) and lines[dy][dx] == char:
                    queue.append((dx, dy))
                
    # Return the set of points in the area
    return area
            
# Get a list of areas in the lines
def get_areas(lines):
    
    # Set of points we have assigned to an area
    explored = set()
    
    # Init a list
    areas = []
    
    # For every point
    for y, _ in enumerate(lines):
        for x, _ in enumerate(lines[y]):
            
            # If we have not yet assigned it to an area
            if (x, y) in explored:
                continue
            
            # Get the area for the point
            area = get_area(x, y, lines)
            
            # Add all points to list of explored points
            explored |= area
            
            # Add the area to the list
            areas.append(area)
            
    return areas

# Get the perimeter of an area
def get_area_perimeter(area):
    
    # Direction we can explored
    dirs = [(1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]
    
    # Init perimeter as zero
    perimeter = 0
    
    # For every point in the area
    for x, y in area:
        
        # For every direction
        for dx, dy in dirs:
            
            # If the point is not in the area, it is on the perimeter
            # increment it
            if (x + dx, y + dy) not in area:
                perimeter += 1
    
    # Return the perimeter
    return perimeter

# Get fences in a specific direction 
def get_fences_in_direction(area, dx, dy):
    
    # List of fences
    fences = []
    
    # For every point in the area
    for px, py in area:
        
        # Get the point in the given direction
        fx = px + dx
        fy = py + dy
        
        # If the point is in the area, it is not a fence
        if (fx, fy) in area:
            continue
        
        # Create a new set, add the fence and add it to the list
        new_fence_set = set()
        new_fence_set.add((fx, fy))
        
        fences.append(new_fence_set)
    
    # Return the list of faces
    return fences

# Determine if two groups of fences are connected
def is_same_group(fence_group_1, fence_group_2):
    
    # The directions we can go in
    dirs = [(1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]
    
    # For every pair of groups of fences
    for p1x, p1y in fence_group_1:
        for p2x, p2y in fence_group_2:
            
            # For every direction
            for dx, dy in dirs:
                
                # If the fences are adjoining, return true
                if p1x + dx == p2x and p1y + dy == p2y:
                    return True
                
    # Otherwise return false
    return False

# Group fences into adjoining groups
def group_fences(fences):
    
    # Keep joining until no changes are found
    change_found = True
    
    while change_found:
        
        # Assume no changes
        change_found = False
        
        # Init vars for indices of adjoining sets
        merge_1 = -1
        merge_2 = -1
        
        # For every pair of fence groups
        for i, fence_group_1 in enumerate(fences):
            for j, fence_group_2 in enumerate(fences):
                if i == j:
                    continue
                
                # If they are in the same group, mark change found
                if is_same_group(fence_group_1, fence_group_2):
                    merge_1 = i
                    merge_2 = j
                    change_found = True
                    break
                
            if change_found:
                break
      
        # If we have found a change, add group 2 to group 1 and remove group 2
        if change_found:
            fences[merge_1] |= fences[merge_2]
            fences = fences[:merge_2] + fences[merge_2+1:]
    
    # Return the list of fences
    return fences

# Get the number of sides for an area
def get_area_sides(area):
    
    # Init as zero
    sides = 0
    
    # List of directions
    dirs = [(1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]
    
    # For every direction
    for dx, dy in dirs:
        
        # Get the fences that face the directions
        fences_in_direction = get_fences_in_direction(area, dx, dy)
        
        # Group the fences
        fences_in_direction = group_fences(fences_in_direction)
        
        # Add the number of groups to the number of sides
        sides += len(fences_in_direction)
                
        
    # Return the number of sides
    return sides

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Get every area
areas = get_areas(lines)

# Init vars for results
total_price = 0
total_price_bulk = 0

# For every area
for area in areas:
    
    # Get perimeter, area and number of sides
    area_perimeter = get_area_perimeter(area)
    area_area = len(area)
    area_sides = get_area_sides(area)
    
    # Add area result to totals
    
    total_price += area_perimeter * area_area
        
    total_price_bulk += area_area * area_sides
    
# Print the results
print(f'{total_price} is the total price of fences')
print(f'{total_price_bulk} is the total price of fences when buying in bulk')
