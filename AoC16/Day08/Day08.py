# Need numpy for array processing
import numpy as np

# Function to create a rectange in the upper left of the screen
def rect(screen, A, B):
    screen[0:B,0:A] = np.ones((B,A),dtype=bool)
    return screen

# Function to rotate column x by n
def rotateColumn(screen, x, n):
    screen[:,x] = np.concatenate((screen[-n:,x], screen[0:-n,x]))
    return screen

# Function to rotate column y by n
def rotateRow(screen, y, n):
    screen[y,:] = np.concatenate((screen[y,-n:], screen[y,0:-n]))
    return screen

# Function to print the screen
def printScreen(screen):
    for i in screen:
        for j in i:
            print('#' if j else '.', end='')
        print()

# Open input and read as lines
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# Create the empty screen
screen = np.zeros((6, 50), dtype = bool)

# For every instruction
for i in instructions:
    
    # Split the line to parse it easier
    split = i.split(' ')
    
    # Perform the specified action
    if split[0] == 'rect':
        A, B = int(split[1].split('x')[0]), int(split[1].split('x')[1])
        screen = rect(screen, A, B)
    elif split[1] == 'column':
        A, B = int(split[2].split('=')[1]), int(split[-1])
        rotateColumn(screen, A, B)
    else:
        A, B = int(split[2].split('=')[1]), int(split[-1])
        rotateRow(screen, A, B)

# Print the results
print(f'{sum(sum(screen))} pixels light up on the screen')
print('The output of the screen is the following:')
printScreen(screen)