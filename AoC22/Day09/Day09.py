# Function to create a rope of a given length
# Just a list of tuples
def createRope(length):
    return [(0,0) for i in range(length)]
    
# Function to tell if two knots on the rope are apart
def isApart(head, tail):
    
    # If either horizontal or vertical distance is over 1, return True
    if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
        return True
    return False

# Function to align to knots on a rope
def align(head, tail):
    
    # If the ropes are not apart, do nothing
    if not isApart(head, tail):
        return tail
    
    # Determine directions to use to catch up
    right = 1 if head[0]-tail[0] > 0 else -1
    up = 1 if head[1]-tail[1] > 0 else -1 

    # Tail is diagonaly offset
    # Take one diagonal step. Use current position to determine which direction
    if abs(head[0]-tail[0]) + abs(head[1]-tail[1]) > 2:       
        return (tail[0]+right, tail[1]+up)
    
    # Tail is horizontally offset
    # Take one horizontal step
    if head[1] == tail[1]:
        return (tail[0]+right, tail[1])
    
    # Tail is vertically offset
    # Take one vertical step
    if head[0] == tail[0]:
        return (tail[0], tail[1]+up)    

# Perform moves in a direction
def move(direction, dist, rope):
    
    # Set of newly visited nodes
    visited = set()
    
    # Determine which way to move
    move = (0,0)
    if direction == "L":
        move = (-1,0)
    elif direction == "R":
        move = (1,0)
    elif direction == 'U':
        move = (0,-1)
    elif direction == "D":
        move = (0,1)
        
    # For every step to move
    for i in range(dist):
        
        # Move the head
        rope[0] = (rope[0][0]+move[0], rope[0][1]+move[1])
        
        # For every pair of knots, align
        for j in range(len(rope)-1):
            rope[j+1] = align(rope[j], rope[j+1])
            
        # Add the position of the end to the visited set
        visited.add(rope[-1])
                
    # Return the new rope and the points it has visited
    return (rope, visited)


# Read and parse the input
f = open('input.txt', 'r')
moves = f.read().split('\n')

# Create the two ropes
rope = createRope(2)
longRope = createRope(10)

# Create the two sets of visited points
visited = set()
longVisited = set()

# For every move
for m in moves:
    
    # Split and parse
    direction, dist = m.split()[0], int(m.split()[1])
    
    # Perform move on both ropes
    rope, newVisits = move(direction, dist, rope)
    longRope, newLongVisits = move(direction, dist, longRope)
    
    # Add the moves to the sets
    visited |= newVisits
    longVisited |= newLongVisits
    
# Print the results
print(f'Using a rope of length 2, {len(visited)} points are visited by the end')
print(f'Using a rope of length 10, {len(longVisited)} points are visited by the end')
