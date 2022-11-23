# Need numpy to multiply lists
import numpy as np

# Parses the input into tuples
def parse(specs):
    
    # Empty list initially
    discs = []
    
    # For every input string
    for s in specs:
        
        # Split it to parse easier
        s = s.split()
        
        # Find the number of positions and the current position
        numPos = int(s[3])
        pos = int(s[-1][0:-1])
        
        # Add them to the list
        discs.append((numPos, pos))
        
    # Return the lists
    return discs
    
# Get the time to press the button, given the list of discs
def getTime(discs):
    
    # Start at time 0
    time = 0
    
    # Loop until we find a solution
    while True:
        
        # Lists of discs we can pass through at the current time
        hits = []
        
        # For every discs
        for i, d in enumerate(discs):
            
            # Check if we can hit it in the current time 
            if (d[1]+time+(i+1)) % d[0] == 0:
                hits.append(d[0])
        
        # If we can hit all discs, return the current time
        if len(hits) == len(discs):
            return time
        
        # If we can hit some discs, find the next time we can hit thoses discs
        elif len(hits) > 0:
            time += np.prod(hits)
            
        # Else just increment the time
        else:
            time += 1
                    
        
                
# Open input and read as lines
f = open('input.txt', 'r')
specs = f.read().split('\n')

# Parse the input
discs = parse(specs)

# Find the time to press the button
roundOne = getTime(discs)

# Add the new disc to the list
discs.append((11, 0))

# Find the time to press the button the next time
roundTwo = getTime(discs)

# Print the results
print(f'The time to press the button is {roundOne}')
print(f'The time to press the button when the new disc is added is {roundTwo}')