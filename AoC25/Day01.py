# Parse the lines into a list of instructions
def parse(lines):
    
    instructions = []
    
    for line in lines:
        
        direction, distance = line[0], line[1:]
        
        instructions.append((direction, int(distance)))
        
    return instructions

# Count how many times the dial ends at zero
def count_zeroes(instructions, starting_point, size):
    
    # Init result as zero
    zeroes = 0

    # Init the position
    position = starting_point
    
    # For every direction and length in the instruction
    for direction, length in instructions:
        
        # Turn either clockwise or anticlockwise
        if direction == 'L':
            position -= length
        else:
            position += length
            
        # Perform mod so that we are within bounds
        position %= size
        
        # If we are at zero, increment
        if position == 0:
            zeroes += 1
            
    return zeroes

# Count how many times the dial turns to zero, including when it just
# passes through
def count_zero_clicks(instructions, starting_point, size):
    
    # Init result as zero
    zeroes = 0

    # Init the position
    position = starting_point
    
    # For every direction and length in the instruction
    for direction, length in instructions:
        
        # Find out how many full rotations the instruction results in
        full_rotations = length // size
        
        # Add the number of full  rotations to the number of zeroes
        zeroes += full_rotations
        
        # Remove full rotations from length
        length -= full_rotations * size
        
        # Turn either clockwise or anticlockwise
        if direction == 'L':
            next_pos = position - length
        else:
            next_pos = position + length
                            
        # Turn one at a time
        while position != next_pos:
            
            if next_pos > position:
                position += 1
            else:
                position -= 1
                
            # Check if position is zero. Increment if so
            if position % size == 0:
                zeroes += 1
                
    # Return the number of zeroes
    return zeroes


# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the instruction
instructions = parse(lines)

# Init problem variables
starting_point = 50
size = 100

# Count zeroes using both methods
zeroes = count_zeroes(instructions, starting_point, size)
zero_clicks = count_zero_clicks(instructions, starting_point, size)

# Print the results
print(f'The dial ends at zero {zeroes} times')
print(f'The passes over zero {zero_clicks} times')

# Too high
# 6972
# too low
# 6698