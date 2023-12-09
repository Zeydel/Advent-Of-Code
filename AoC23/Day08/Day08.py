# Function to find the greatest common divisor between two numbers
def greatest_common_divisor(a, b):
    
    if (b == 0):
        return a
    return greatest_common_divisor(b, a % b)

# In conjunction with above function, finds the least common multiple between a list of numbers
def least_common_multiple(numbers):
    
    lcm = 1
    
    # After i iterations, lcm contains the lcm between numbers[0]...numbers[i-1]
    for n in numbers:
        lcm = (n * lcm) // (greatest_common_divisor(n, lcm))
        
    return lcm

# Read and parse the input
f = open('input.txt', 'r')
desertMap = f.read().split('\n')

# Take the direction line from the map
directions = desertMap[0]

# Init a node dictionary. We keep it as a tree-like structure
nodes = {}

# For every line, split into source, left and right
for node in desertMap[2:]:
    
    src = node.split(' = ')[0]
    
    left = node.split(' = (')[1].split(', ')[0]
    
    right = node.split(', ')[1].split(')')[0]
    
    # Add it to the dictionary
    nodes[src] = (left, right)

# Number of steps taken
stepCounter = 0

# Current location
curNode = 'AAA'

# While we haven't reached the end
while curNode != 'ZZZ':
    
    # Get the next instruction
    instruction = directions[stepCounter % len(directions)]
    
    # Take the correct step
    if instruction == 'L':
        curNode = nodes[curNode][0]
    else:
        curNode = nodes[curNode][1]
    
    stepCounter += 1
    
# Get a list of starting nodes
curNodes = []
for n in nodes:
    if n[-1] == 'A':
        curNodes.append(n)
        
# List of number of steps needed to reach each end
finishSteps = [-1 for i in curNodes]

# Number of steps taken
ghostStepCounter = 0

# While we havent reached the end for any of the starting points
while any([i == -1 for i in finishSteps]):
    
    # Find the next insruction
    instruction = directions[ghostStepCounter % len(directions)]
    
    ghostStepCounter += 1
    
    # Take the step for every current node
    for i, c in enumerate(curNodes):
        if instruction == 'L':
            curNodes[i] = nodes[c][0]
        else:
            curNodes[i] = nodes[c][1]
            
        # If we have reached the end, and we havent reached an end before, remember it
        if curNodes[i][-1] == 'Z' and finishSteps[i] == -1:
            finishSteps[i] = ghostStepCounter
    
    
# Print the results
print(f'It takes {stepCounter} steps to reach the end')
print(f'It takes {least_common_multiple(finishSteps)} steps to reach the end for every starting point')