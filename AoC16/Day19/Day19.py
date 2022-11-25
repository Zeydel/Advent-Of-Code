# Function to get the winning elf
def getWinner(elves):
    
    # While there is more than one elf left
    while len(elves) > 1:
        # If there is an even amount of elves
        if len(elves) % 2 == 0:
            # Remove every other elf
            elves = [i for i in elves[::2]]
        else:
            # Remove every other elf and also the first one
            elves = [i for i in elves[2::2]]
        
    # Return the only elf left
    return elves[0]
    
# This just works apparently. Derived from the pattern of the result of
# the first hundred results
def getWinnerAcross(numElves):
    
    i = 1
    
    while i*3 < numElves:
        i *= 3
        
    return numElves-i

# Puzzle input
numElves = 3004953
        
# Create a list of elves
elves = [i for i in range(1, numElves+1)]

# Print the results
print(f'The winning elf is {getWinner(elves)}')
print(f'With the new playstyle, the winning elf is {getWinnerAcross(numElves)}')
