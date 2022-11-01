# Function to find the floor that santa ends up in
def findFinalFloor(directions):
    # Santa is initially on floor 0
    floor = 0
    # Change floor depending on instruction
    for d in directions:
        if d == '(':
            floor += 1
        else:
            floor -= 1
    # Return the final floor
    return floor

# Find the first time that santa enters the basement
def findFirstBasementEntry(directions):
    # Start on floor 0
    floor = 0
    
    # Change floor depending on instruction. Keep track of current instruction
    for c, d in enumerate(directions):
        if d == '(':
            floor += 1
        else:
            floor -= 1
            # If we have just descended, check if we entered the basement
            if floor == -1:
                return c + 1 # Add one to fix the off by one error
            
    # Return -1 if we havent found anything. This shouldn't happen
    return -1

# Read input as one long string
f = open('input.txt', 'r')
directions = f.read()

# Print the solutions
print(f'Santa ends up on floor {findFinalFloor(directions)}')
print(f'Santa first enters the basement on instruction {findFirstBasementEntry(directions)}')