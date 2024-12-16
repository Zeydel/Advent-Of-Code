# Parse input into bot position, walls, boxes and instructions
def parse(lines):
    
    bot_pos = (-1, -1)
    walls = set()
    boxes = set()
    
    break_line = -1 
        
    for y, line in enumerate(lines):
                
        if len(line) == 0:
            break_line = y
            break
        
        for x, char in enumerate(line):
            
            if char == '#':
                walls.add((x, y))
            elif char == 'O':
                boxes.add((x, y))
            elif char == "@":
                bot_pos = (x, y)
                
    instructions = ''
    
    for i in range(break_line + 1, len(lines)):
        instructions += lines[i]
        
    return bot_pos, walls, boxes, instructions
    
# Parse input into bot position, walls, boxes and instructions
# but for the wide version of the map
def parse_wide(lines):
    
    bot_pos = (-1, -1)
    walls = set()
    boxes = set()
    
    break_line = -1 
    
    for y, line in enumerate(lines):
        
        if len(line) == 0:
            break_line = y
            break
        
        for x, char in enumerate(line):
            
            if char == '#':
                walls.add((x*2, y))
                walls.add(((x*2)+1, y))
            elif char == 'O':
                boxes.add(((x*2, y), ((x*2)+1, y)))
            elif char == "@":
                bot_pos = (x*2, y)
                
    instructions = ''
    
    for i in range(break_line + 1, len(lines)):
        instructions += lines[i]
        
    return bot_pos, walls, boxes, instructions

# Get a box position from the set of boxes if it exists, otherwise
# return -1
def get_box(boxes, pos):
    
    for box1, box2 in boxes:
        
        if box1 == pos or box2 == pos:
            return (box1, box2)
        
    return -1

# Map the direction to the input to its direction coordinate
def get_direction(instruction):
    
    if instruction == '^':
        return (0, -1)
    if instruction == 'v':
        return (0, 1)
    if instruction == '<':
        return (-1, 0)
    if instruction == '>':
        return (1, 0)
            
# Move the box based on the input
def move(bot_pos, walls, boxes, instruction):
    
    # Get the bot position
    bx, by = bot_pos
    
    # Get the direction to move
    dx, dy = get_direction(instruction)
        
    # Init a set of boxes to move
    move_set = set()
    
    # Compute the new coordinate of the bot
    nx, ny = bx + dx, by + dy
    
    # While we are not in a free space
    while (nx, ny) in walls or (nx, ny) in boxes:
        
        # If we see a wall, return the initial values
        if (nx, ny) in walls:
            return bot_pos, boxes
        
        # If we see a box, add it to the set of boxes to move
        move_set.add((nx, ny))
        
        # Increment direction
        nx += dx
        ny += dy
            
    # Remove all boxes in set to remove
    for move_box in move_set:
        boxes.remove(move_box)
        
    # Add all boxes back in their new position
    for move_box_x, move_box_y in move_set:
        boxes.add((move_box_x + dx, move_box_y + dy))
        
    # Compute new bot position
    bot_pos = (bx + dx, by + dy)
    
    return bot_pos, boxes

# Move, but wide
def move_wide(bot_pos, walls, boxes, instruction):
    
    # Get bot pos
    bx, by = bot_pos
    
    # Get direction to move
    dx, dy = get_direction(instruction)
        
    # Init set of boxes to move
    move_set = set()
    
    # If we are gonna go into a wall immideately, retun initial values
    if (bx + dx, by + dy) in walls:
        return bot_pos, boxes
        
    # Get the box we will go into when we move and add it to move set
    # if it exists
    box = get_box(boxes, (bx + dx, by + dy))
    
    if box != -1:
        move_set.add(box)
        
    # If there is no box, there is nothing to move. Do not initiate loop
    search = True
    
    if len(move_set) == 0:
        search = False
    
    # While we are searching
    while search:
        
        # Count the number of boxes to move
        boxes_count = len(move_set)
        
        # Set of new boxes
        new_boxes = set()
        
        # For every box in the move set
        for box1, box2 in move_set:
            
            # If it hits a wall, return initial values
            if (box1[0] + dx, box1[1] + dy) in walls:
                return bot_pos, boxes
            if (box2[0] + dx, box2[1] + dy) in walls:
                return bot_pos, boxes
            
            # Get both new boxes it will hit and add to move set,
            # if they exists
            new_box1 = get_box(boxes, (box1[0] + dx, box1[1] + dy))
            
            if new_box1 != -1:
                new_boxes.add(new_box1)
            
            new_box2 = get_box(boxes, (box2[0] + dx, box2[1] + dy))
            
            if new_box2 != -1:
                new_boxes.add(new_box2)
        
        # Add the boxes found
        move_set |= new_boxes    
            
        # If we havent added new boxes, stop search
        if boxes_count == len(move_set):
            search = False
                    
    # Remove and add back boxes in their new position
    for box1, box2 in move_set:
        boxes.remove((box1, box2))
        
    for box1, box2 in move_set:
        boxes.add(((box1[0] + dx, box1[1] + dy), (box2[0] + dx, box2[1] + dy)))
        
    # Get new bot pos
    bot_pos = (bx + dx, by + dy)
    
    # Return bot pos and boxes
    return bot_pos, boxes
    
# Do every instruction and return new bot pos and boxes
def do_instructions(bot_pos, walls, boxes, instructions):
    
    for instruction in instructions:
        bot_pos, boxes = move(bot_pos, walls, boxes, instruction)
        
    return bot_pos, boxes
    
# Do every instruction and return new bot pos and boxes
# but wide
def do_instructions_wide(bot_pos, walls, boxes, instructions):
    
    for instruction in instructions:
        bot_pos, boxes = move_wide(bot_pos, walls, boxes, instruction)
        
    return bot_pos, boxes
            
# Get the sum of coordinates
def get_coordinte_sum(boxes):
    
    coordinate_sum = 0
    
    for box_x, box_y in boxes:
        
        coordinate_sum += (box_y * 100) + box_x
        
    return coordinate_sum

# Get the sum of coordinates, but wide
def get_coordinate_sum_wide(boxes, lines):
    
    coordinate_sum = 0
    
    for box1, box2 in boxes:
        
        coordinate_sum += (box1[1] * 100) + box1[0]
        
    return coordinate_sum

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
bot_pos, walls, boxes, instructions = parse(lines)

# Do every instruction
bot_pos, boxes = do_instructions(bot_pos, walls, boxes, instructions)

# Get coordinate sum
coordinate_sum = get_coordinte_sum(boxes)

# Parse input again, but wide
bot_pos, walls, boxes, instruction = parse_wide(lines)

# Do every instruction, but wide
bot_pos, boxes = do_instructions_wide(bot_pos, walls, boxes, instructions)

# Get coordinate sum, but wide
coordinate_sum_wide = get_coordinate_sum_wide(boxes, lines)

print(f'{coordinate_sum} is the sum of distances to every box')
print(f'{coordinate_sum_wide} is the sum of distances to every box, but wide')