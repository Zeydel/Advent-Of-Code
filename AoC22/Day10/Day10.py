# Need numpy for 2d array stuff
import numpy as np

# Function to draw the canvas
def drawCanvas(canvas):
    
    # Iterate through
    for i in range(canvas.shape[0]):
        for j in range(canvas.shape[1]):
            # Put a # if true, else put a .
            print('■' if canvas[i,j] else ' ', end="")
        print()

# Open input and read as strings
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# Init the variables
strength = 1
cycle = 1

# The cycles of the values we want to save
strengths = {
    20:  -1,
    60:  -1,
    100: -1,
    140: -1,
    180: -1,
    220: -1
    }

# Create a canvas and flatten it
canvas = np.zeros((6,40), dtype=bool)
canvas = canvas.reshape(6*40)

# For every instruction
for i in instructions:
    
    # Split to parse
    split = i.split()
    
    #BEFORE
    
    # Determine the operation and set some values
    if split[0] == "addx":
        V = int(split[1])
        rounds = 2
    else:
        V = 0
        rounds = 1
        
    
    #DURING
    
    # For the time of the operation
    for i in range(rounds):
        
        # Draw a pixel
        if (cycle-1)%40 in range(strength-1, strength+2):
            canvas[cycle-1] = True            
        
        # Save the cycle value if we need it
        if cycle in strengths:
            strengths[cycle] = strength
        
        # Increment the cycle
        cycle += 1
        
    
    #AFTER
    
    # Add the value to the strength
    strength += V
    
# Restore canvas shape
canvas = canvas.reshape((6,40))

print(f'The sum of the signal strengths is {sum([k*strengths[k] for k in strengths])}')
print(f'The image on the screen is')
drawCanvas(canvas)
