# Import numpy for smart 2d array processing
import numpy as np

# Function to turn on a subarray
def turnOn(lights, xs, ys, xe, ye):
    lights[xs:xe+1,ys:ye+1] = np.ones(((xe-xs)+1,(ye-ys)+1),dtype=bool)
    return lights
    
# Function to turn off a subarray
def turnOff(lights, xs, ys, xe, ye):
    lights[xs:xe+1,ys:ye+1] = np.zeros(((xe-xs)+1,(ye-ys)+1),dtype=bool)
    return lights
    
# Function to binary negate a subarray
def toggle(lights, xs, ys, xe, ye):
    lights[xs:xe+1,ys:ye+1] = ~lights[xs:xe+1,ys:ye+1]
    return lights

# Function that takes a list of instructions and outputs the final lighting
# configutarion
def getFinalLightConfig(strings):
    
    # Start with all lights off
    lights = np.zeros((1000,1000), dtype=bool)
    
    # For every string
    for s in strings:
        
        # Do some parsting
        s = s.replace(',', ' ')
        split = s.split(' ')
    
        # Perform action according to instruction
        if split[1] == 'on':
            lights = turnOn(lights, int(split[2]), int(split[3]), int(split[5]), int(split[6]))
        elif split[1] == 'off':
            lights = turnOff(lights, int(split[2]), int(split[3]), int(split[5]), int(split[6]))
        else:
            lights = toggle(lights, int(split[1]), int(split[2]), int(split[4]), int(split[5]))
            
    # Return the lights after all instructions have been performed
    return lights

# Function to increment subarray
def turnOnInt(lights, xs, ys, xe, ye):
    lights[xs:xe+1,ys:ye+1] += 1
    return lights
    
# Function to decrement subarray, lower bounded by zero
def turnOffInt(lights, xs, ys, xe, ye):
    lights[xs:xe+1,ys:ye+1] -= 1
    lights[lights<0] = 0
    return lights
    
# Function to add two to subarray
def toggleInt(lights, xs, ys, xe, ye):
    lights[xs:xe+1,ys:ye+1] += 2
    return lights

# Function that takes a list of instructions and outputs the final lighting
# configutarion, when lights have integer values
def getFinalLightConfigInt(strings):
    
    # Start with all lights off
    lights = np.zeros((1000,1000), dtype=int)
    
    # For every string
    for s in strings:
        
        # Do some paring
        s = s.replace(',', ' ')
        split = s.split(' ')
    
        # Perform action according to instruction
        if split[1] == 'on':
            lights = turnOnInt(lights, int(split[2]), int(split[3]), int(split[5]), int(split[6]))
        elif split[1] == 'off':
            lights = turnOffInt(lights, int(split[2]), int(split[3]), int(split[5]), int(split[6]))
        else:
            lights = toggleInt(lights, int(split[1]), int(split[2]), int(split[4]), int(split[5]))
    
    # Return the lights after all instructions have been performed
    return lights


# Read input as lines
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Print the results
print(f'{np.sum(getFinalLightConfig(strings))} lights are lit when the lights have boolean values')
print(f'{np.sum(getFinalLightConfigInt(strings))} lights are lit when the lights have integer values')