# Parse the first part of the input
# into a list of stacks
def parse(stack):
    
    # Split on newline and make a number of stacks according to 
    # the number of elements in the last line
    split = stack.split('\n')
    stacks = [[] for i in split[-1].split()]
    
    # For every line, extract the crate names and put them in their stacks
    for l in split[:-1]:
        for i, c in enumerate([l[i:i+3] for i in range(0, len(l), 4)]):
            if c == '   ':
                continue
            stacks[i].insert(0, c[1])
        
    # Return the stacks
    return stacks

# Move the stacks according to the instructions
def move(stacks, instructions):
    
    # For every instruction
    for i in instructions.split('\n'):
        
        # Split and extract amount, from and to 
        split = i.split(' ')
        a, f, t = int(split[1]), int(split[3]), int(split[5])
        
        # a, times pop from one stack and add to the other
        for i in range(a):
            stacks[t-1].append(stacks[f-1].pop())
            
    # Return the stacks
    return stacks

# Move the stacks with the new crane
def move9001(stacks, instructions):
    
    # For every instruction
    for i in instructions.split('\n'):
        
        # Split and extract amount, from and to
        split = i.split(' ')
        a, f, t = int(split[1]), int(split[3]), int(split[5])
        
        # Move the a crates from f to t
        stacks[t-1] += stacks[f-1][-a:]
        
        # Delete from f
        del stacks[f-1][-a:]
        
    # Return the stacks
    return stacks

# Get the results
def getResult(stacks):
    
    # Empty string
    result = ''
    
    # Add the top crate from every stack
    for s in stacks:
        result += s[-1]
        
    return result

# Read and parse the input
f = open('input.txt', 'r')
stack, instructions = f.read().split('\n\n')

# Parse the stacks to times
stacks = parse(stack)
stacks9001 = parse(stack)

# Move the stacks around in both ways
stacks = move(stacks, instructions)
stacks9001 = move9001(stacks9001, instructions)

# Print the results
print(f'Using the CrateMover 9000, the result is {getResult(stacks)}')
print(f'Using the CrateMover 9001, the result is {getResult(stacks9001)}')