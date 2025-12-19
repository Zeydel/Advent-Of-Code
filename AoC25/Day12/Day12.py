# Parse the input into shapes and grids
def parse(lines):
    
    shapes = []
    grids = []
    
    shape = []
    
    for line in lines:
        
        if line == '':
            shapes.append(shape)
            shape = []
            y = 0
            continue
        
        if 'x' not in line and ':' in line:
                        
            continue
        
        if 'x' in line:
            
            splits = line.split()
            
            x, y = [int(n) for n in splits[0][:-1].split('x')]
            
            grids.append(((min(x, y), max(x, y)), [int(n) for n in splits[1:]]))

            continue
            
        shape.append([char for char in line])
            
                
    return shapes, grids

# Count how many of the points in the shape are filled in
def get_shape_sizes(shapes):
    
    shape_sizes = []
    
    for shape in shapes:
        
        size =  0
        
        for line in shape:
            for char in line:
                
                if char == '#':
                    size += 1
                    
        shape_sizes.append(size)
        
    return shape_sizes
    
# Figure out if the total area of the shapes is larger than the total area of the grid
def is_impossible_fit(shape_sizes, grid):
    
    grid_sizes, shapes_to_fit = grid
    
    grid_size = grid_sizes[0] * grid_sizes[1]
    
    total_shape_size = 0
    
    for i, shape in enumerate(shapes_to_fit):
        
        total_shape_size += shape_sizes[i] * shape
        
    return total_shape_size > grid_size

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
shapes, grids = parse(lines)

# Get the sizes of the shapes
shape_sizes = get_shape_sizes(shapes)

# Init possible grids as zero
possible_grids = 0

# For every grid in grids
for grid in grids:
    
    # If the grid is not impossible, increment possible grids
    if not is_impossible_fit(shape_sizes, grid):
        possible_grids += 1
        
# Print the result
print(f'{possible_grids} regions can fit all the presents')