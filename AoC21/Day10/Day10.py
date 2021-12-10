import math
from collections import deque

# Function to get completion score given a stack and the map of completion points
def get_completion_score(stack, completion_points):
    
    # Init score
    score = 0
    
    # While the stack is not empty
    while stack:
        
        # Multiply the score by 5 and add the completion score
        score *= 5
        score += completion_points[stack.pop()]
        
    # Return the calculated score
    return score

# Open file and read as list of strings
f = open('input.txt', 'r')
lines = f.read().split('\n')

# List of opening brackets
open_chars = ['(', '[', '{', '<']

# Maps from opening bracket to closing brackets
char_map = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

# Maps from closing bracket to points
char_points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

# Maps from opening bracket to completion points
completion_points = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

# Init vars for result
score = 0
completion_scores = []

# For each line
for l in lines:
    
    # Create new stack
    stack = deque()
    
    # Assume that the line is not corrupted
    corrupted = False
    
    # For each char in line
    for c in l:
        
        # If c opening bracket, push it to the stack
        if c in open_chars:
            stack.append(c)
        else:
            
            # Else pop from stack
            p = stack.pop()
            
            # If current char is not corresponding closer to popped opener, the string is corrupted
            if not c == char_map[p]:
                
                # Add to score and set that string is corrupted
                score += char_points[c]
                corrupted = True
                break
            
    # If string is not corrputed, caluclate the completion score and add it to the list
    if not corrupted:
        completion_scores.append(get_completion_score(stack, completion_points))
    
# Sort the completion scores. Needed for getting median
completion_scores = sorted(completion_scores)
   
# Print the results
print('The total syntax error score for the errors is ' + str(score))
print('The middle completion score is ' + str(completion_scores[math.floor(len(completion_scores)/2)]))