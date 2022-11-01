# We need regex
import re

# Function for getting summing the lengths of strings
def totalLength(strings):
    return sum([len(s) for s in strings])

# Function to reduce strings
def reduceStrings(strings):
    reducedStrings = []
    
    # For every string
    for s in strings:
        
        # Remove the double quotes
        s = s[1:len(s)-1]
        
        # Replace \" with 1
        s = re.sub(r'\\"','1',s)
        
        # Replace \\ with 1
        s = re.sub(r'\\\\','1',s)
        
        # Replace hex characters with 1
        s = re.sub(r'\\x[0-9a-f][0-9a-f]','1',s)
    
        # Add new string to list
        reducedStrings.append(s)
        
    # Return the list of reduced strings
    return reducedStrings

# Function to expand strings
def expandStrings(strings):
    expandedStrings = []
    
    # For every string
    for s in strings:
        
        # Replace " with 11
        s = re.sub(r'\"','11',s)
        
        # Replace \ with 11
        s = re.sub(r'\\','11',s)
        
        # Add quotes on both ends
        s = "\"" + s + "\""
        
        # Add expanded string to list
        expandedStrings.append(s)
    return expandedStrings

# Read as strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Get original total length
rawLength = totalLength(strings)

# Reduce strings and get their total length
reducedStrings = reduceStrings(strings)
reducedLength = totalLength(reducedStrings)

# Expand strings and get their total length
expandedStrings = expandStrings(strings)
expandedLength = totalLength(expandedStrings)

# Print the result
print(f'Original length minus the reduced length is {rawLength - reducedLength}')
print(f'Expanded length minus the originial length is {expandedLength - rawLength}')