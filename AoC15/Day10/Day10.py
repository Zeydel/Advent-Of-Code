# This makes it a lot easier
from itertools import groupby

# Function to get the next iteration of the game
def expand(number):
    
    # Init an empty string
    output = ""
    
    # Split the string into groups of the same consecutive number
    split = ["".join(group) for ele, group in groupby(number)]
    
    # For every group
    for s in split:
        
        # Append its length and character to the output
        output += str(len(s)) + s[0] 
        
    # Return it
    return output 

# The initial string
input = '3113322113'

answerAfter40 = ''

# Perform 40 expansions
for i in range(40):
    input = expand(input)
    
# Save the answer
answerAfter40 = len(input)

# Perform 10 more expansions
for i in range(10):
    input = expand(input)

# Print the results
print(f'After 40 rounds, the string is {answerAfter40} characters long')
print(f'After 40 rounds, the string is {len(input)} characters long')
