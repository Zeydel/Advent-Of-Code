import numpy as np

# Function to fold the paper
def fold(instruction, paper):
    
    # Find folding axis and index
    axis = instruction.split('=')[0][-1]
    index = int(instruction.split('=')[1])
    
    # If we are folding along a horizontal line
    if axis == 'y':
        
        # Split paper into up and down. Flip down upside down
        paper_u = paper[:index,:]
        paper_d = np.flipud(paper[index + 1:,:])
        
        # Go through down. If we see a #, put it in up
        for iy, ix in np.ndindex(paper_u.shape):
            if paper_d[iy,ix] == '#':
                paper_u[iy,ix] = '#'
                
        # Return the paper
        return paper_u
    
    # If we are folding along a vertical line
    if axis == 'x':
        
        # Split paper into left and right
        paper_l = paper[:,:index]
        paper_r = np.fliplr(paper[:,index + 1:])
        
        # Go through right, if we see a #, put it in left
        for iy, ix in np.ndindex(paper_l.shape):
            if paper_r[iy,ix] == '#':
                paper_l[iy,ix] = '#'
                
        # Return the paper
        return paper_l

# Helper method to print the paper
def print_paper(paper):
    for p in paper:
        print(''.join(p))

# Open input and read as lines
f = open('input.txt', 'r')
lines = f.read().split('\n')

# Init counter for number of coordinates and list of coordinates
i = 0
coordinates = []
for l in lines:
    
    # Increment counter
    i += 1
    
    # If we see an empty line, there are no more coordinates
    if not l:
        break
    
    # Append tuple of coordinate to list
    coordinates.append((int(l.split(',')[0]), int(l.split(',')[1])))

# Empty list of instructions
instructions = []

# Max x and y, used for calculating size of the paper
max_x = 0
max_y = 0

# For each remaining input line
for l in lines[i:]:
    
    # Add the instruction
    instructions.append(l)
    
    # Update x and y if necessary
    if 'x' in l and int(l.split('=')[1]) > max_x:
        max_x = int(l.split('=')[1])

    if 'y' in l and int(l.split('=')[1]) > max_y:
        max_y = int(l.split('=')[1])    

# Create paper and fill with '.'
paper = np.zeros(((max_y * 2) + 1, (max_x * 2) + 1), 'U1')
paper.fill('.')

# For each coordinate, put a #
for c in coordinates:
    paper[c[1],c[0]] = '#'
    
# Make the first fold
paper = fold(instructions[0], paper)

# Count the #s
dot_count = 0
for x in np.nditer(paper):
    if x == '#':
        dot_count += 1
        
# Remove first instruction
instructions.pop(0)

# Perform the remaining folds
for i in instructions:
    paper = fold(i, paper)
        
# Print the results
print(str(dot_count) + ' dots are visible after the first fold')
print_paper(paper)