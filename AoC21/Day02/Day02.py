# Some constants
FORWARD = "forward"
DOWN = "down"
UP = "up"

# Function to get position multiplied by depth
def getFinalPosition(lines):
    pos, depth = 0, 0
    for line in lines:
        splitline = line.split()
        
        # Change parameter based on input
        if splitline[0] == FORWARD:
            pos += int(splitline[1])
        if splitline[0] == DOWN:
            depth += int(splitline[1])
        if splitline[0] == UP:
            depth -= int(splitline[1])
    
    return pos * depth
        
# Function to get position multiplied by depth with aim
def getFinalPositionWithAim(lines):
    pos, depth, aim = 0, 0, 0
    for line in lines:
        splitline = line.split()
        
        # Change parameter based on input
        if splitline[0] == FORWARD:
            pos += int(splitline[1])
            depth += (aim * int(splitline[1]))
        if splitline[0] == DOWN:
            aim += int(splitline[1])
        if splitline[0] == UP:
            aim -= int(splitline[1])
            
    return pos * depth

# Read input and split into lines
f = open('input.txt', 'r')
lines = f.read().split('\n')

# Print the results
print('The depth multiplied by the position of the final position is ' + str(getFinalPosition(lines)))
print('The depth multiplied by the position of the final position using aim is ' + str(getFinalPositionWithAim(lines)))