# Function to get the path in a 2d array between two points, given that
# only one coordinate changes
def getPath(p1, p2):
    # If x coordinates are the same, find the range for y coordinate
    if p1[0] == p2[0]:
        return [(p1[0],i) for i in range(p1[1], p2[1], 1 if p2[1] > p1[1] else -1)]
    # Else y coordinates are the same, so we find the range for x coordinate
    else:
        return [(i,p1[1]) for i in range(p1[0],p2[0], 1 if p2[0] > p1[0] else -1)]

# Open input and read as words
f = open('input.txt', 'r')
steps = f.read().split(', ')

# Start at the center
position = (0,0)

# Representing the directions. Start at the first one
directions = [[1,0], [0,-1], [-1,0], [0,1]]
d=0

# Set to keep track of the visited points
visited = set()

# Var for the first place we visit twice
twice = []

# For every step
for s in steps:
    # Turn either left or right
    if s[0] == 'L':
        d += 1
    else:
        d -= 1
    
    # And make sure we are within the bounds of the array
    d %= len(directions)
    
    # Find the current direction and the length to travel
    cur = directions[d]
    length = int(s[1:])
    
    # Remember current position
    oldPos = position
    
    # Find the new position
    position = (position[0]+(cur[0]*length), position[1]+(cur[1]*length))
    
    # Find the path travelled to the new position
    path = getPath(oldPos, position)
    
    # For every place in the path
    for p in path:
        # Check if we have been here before, if we have, remember it
        if not twice and p in visited:
            twice = p
        visited.add(p)
    
# Print the results
print(f'The end is {sum([abs(p) for p in position])} blocks away')
print(f'The first place we visit twice is {sum([abs(p) for p in twice])} blocks away')