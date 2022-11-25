# To hash stuff
from hashlib import md5

# List of doors
doors = [('U',(-1,0)),('D',(1,0)),('L',(0,-1)),('R',(0,1))]

# Function to get open doors from passcode and path so far
def getOpenDoors(passCode, path):
    
    # Hash the passcode plus the path
    hashed = md5((passCode + path).encode()).hexdigest()
    
    # Return doors that have indices of any letter in the string 'bcdef'
    return [doors[i] for i in range(4) if hashed[i] in 'bcdef']
    

# Function to get the shortest path. Basically BFS
def getShortestsPath(passCode):
    
    # Add the inital state to the set of unexplored states
    initial = ('', (0,0))
    unexplored = [initial]
    
    # While we have unexplored states
    while len(unexplored) > 0:
        
        # Pop the first one
        cur = unexplored.pop(0)
        
        # If we are outside the bounds, continue
        if cur[1][0] < 0 or cur[1][1] < 0 or cur[1][0] > 3 or cur[1][1] > 3:
            continue
        
        # If we are at the end, return the path
        if cur[1] == (3,3):
            return cur[0]
        
        # Add the next positions and paths to the set
        for i in getOpenDoors(passCode, cur[0]):
            unexplored.append((cur[0]+i[0], (cur[1][0]+i[1][0], cur[1][1]+i[1][1])))
    
# Function to get the length of the longest path
def getLongestPath(passCode):
    
    # Add the initial state to the set
    initial = ('', (0,0))
    unexplored = [initial]
    
    # Var for the result
    longest = float('-inf')
    
    # While we have states left to explore
    while len(unexplored) > 0:
        
        # Pop the first one
        cur = unexplored.pop(0)
        
        # If we are outside of bounds, continue
        if cur[1][0] < 0 or cur[1][1] < 0 or cur[1][0] > 3 or cur[1][1] > 3:
            continue
        
        # If we are at the end
        if cur[1] == (3,3):
            
            # And the path is longer than the longest so far
            if len(cur[0]) > longest:
                # Save the longest
                longest = len(cur[0])
            continue
        
        # Add the next positions and paths to the set
        for i in getOpenDoors(passCode, cur[0]):
            unexplored.append((cur[0]+i[0], (cur[1][0]+i[1][0], cur[1][1]+i[1][1])))
            
    # Return the longest 
    return longest

# Print the results
passcode = 'gdjjyniy'
print(f'The shortest path is {getShortestsPath(passcode)}')
print(f'The length of the longest path is {getLongestPath(passcode)}')