# Open input and read as words
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# The keypads
pad = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# -1s are not valid
hardPad = [[-1,-1, 1,-1,-1],
           [-1, 2, 3, 4,-1],
           [ 5, 6, 7, 8, 9],
           [-1,'A','B','C',-1],
           [-1,-1,'E',-1,-1]]

# Vars for the current position and codes
cur = (1,1)
hardCur = (2,0)
code = ''
hardCode = ''

# For every instruction line
for i in instructions:
    # For every symbol
    for d in i:
        
        # Handle each letter
        if d == 'U':
            cur = (max(cur[0]-1,0), cur[1])
        if d == 'D':
            cur = (min(cur[0]+1,2), cur[1])
        if d == 'L':
            cur = (cur[0], max(cur[1]-1,0))
        if d == 'R':
            cur = (cur[0], min(cur[1]+1,2))
            
        # Keep track of the current position
        prev = hardCur
        
        # Handle each letter
        if d == 'U':
            hardCur = (max(hardCur[0]-1,0), hardCur[1])
        if d == 'D':
            hardCur = (min(hardCur[0]+1,4), hardCur[1])
        if d == 'L':
            hardCur = (hardCur[0], max(hardCur[1]-1,0))
        if d == 'R':
            hardCur = (hardCur[0], min(hardCur[1]+1,4))
            
        # If we have reached an illegal position, return to the previous
        if hardPad[hardCur[0]][hardCur[1]] == -1:
            hardCur = prev
        
            
    # Add the characters to the codes
    code += str(pad[cur[0]][cur[1]])
    hardCode += str(hardPad[hardCur[0]][hardCur[1]])
    
print(f'The code is {code}')
print(f'The node code is {hardCode}')