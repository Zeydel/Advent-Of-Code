# Function to determine wheter a space is open
def isOpen(x,y, favoriteNumber):
    # If we are outside of bounds, return false
    if x < 0 or y < 0:
        return False
    # Otherwise, do the calculation
    product = (x*x) + (3*x) + (2*x*y) + y + (y*y) + favoriteNumber
    return bin(product).count("1") % 2 == 0

# Function to find the next possible places to step
def getNextPlaces(x, y, favoriteNumber, depth):
    nextPlaces = []
    
    # For every possible move
    for i in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        # If we havent checked that space yet and it is open
        if not (i[0], i[1]) in explored and isOpen(i[0], i[1], favoriteNumber):
            # Add it to the array
            nextPlaces.append(((i[0], i[1]), depth+1))
        # And add it to the space of explored states
        explored.add((i[0], i[1]))
        
    return nextPlaces
    
# The puzzle input
favoriteNumber = 1358

# Starting state
states = [((1,1),0)]
# Mark the have explored the starting state
explored = {(1,1)}
# Counter for places we can see within 50 steps
steppedOn = 0
# Variable for the number of steps to reach the desired place
steps = -1

# While we havent found the number of steps
while steps == -1:
    # Take the next state in the queue
    cur = states.pop(0)
    
    # Increment counter if we are at or below 50 steps
    if cur[1] <= 50:
        steppedOn += 1
    
    # If we have found the desired state, remember it
    if cur[0] == (31,39):
        steps = cur[1]
    
    # Add the next possible states
    states += getNextPlaces(cur[0][0], cur[0][1], favoriteNumber, cur[1])
    
    
# Print the results
print(f'It takes {steps} to get to (31,39)')
print(f'We can reach {steppedOn} places within 50 steps')
        