# Need regex to recognize markers
import re

# Function to perform a single-pass expansion. Doesn't expand
# markers that themselves are part of an expanded string
def expand(string):
    
    # Go through every character
    index = 0
    while index < len(string):
        
        # If we have gotten to the start of a marker
        if string[index] == '(':
            # Extract the marker data
            marker = re.findall(r'\(\d+x\d+\)', string[index:])[0]
            l, r = marker.strip('()').split('x')
            l, r = int(l), int(r)
            # Expand string as: Data before marker + data marked by marker r times + the part after the marker
            string = string[:index] + string[index+len(marker):index+len(marker)+l]*r + string[index+len(marker)+l:]
            # Skip the part we just expanded and continue
            index += (r*l)
            continue
            
        index += 1
    
    # Return the expanded string
    return string
           
# Function to calculate the length of the fully expanded string
def getExpandedLength(string):
    
    # For every character in the string
    length = 0
    index = 0
    while index < len(string):
        
        # If we have gotten to the start of a marker
        if string[index] == '(':
            # Extract the marker data
            marker = re.findall(r'\(\d+x\d+\)', string[index:])[0]
            l, r = marker.strip('()').split('x')
            l, r = int(l), int(r)
            # Use recursion to add the length of the next l characters r times to the length
            length += r * getExpandedLength(string[index+len(marker):index+len(marker) + l])
            # Skip the part we just added and continue
            index += len(marker) + l
            continue
        else: # If its just a normal character, just add one to the counter
            length += 1
        
        index += 1
    
    # Return the found length
    return length

# Open input and read the string
f = open('input.txt', 'r')
string = f.read()

# Exand the string once
expanded = expand(string)

# Print the results
print(f'The length of the singly expanded string is {len(expanded)}')
print(f'The length of the fully expanded string is {getExpandedLength(string)}')
