# Get the number of differences, given a pattern and an index of reflection
def get_differences(pattern, i):
    
    differences = 0
    
    # For every line on each side
    for a, b in zip(pattern[i-1::-1], pattern[i:]):
        
        # Sum the number of differences between characters
        differences += sum([1 for c1, c2 in zip(a,b)if c1 != c2])
        
    return differences

# Get the pattern value sum, given a list of patterns, and a number of differences
# the reflected patterns should have
def get_pattern_value_sum(patterns, differences = 0):
    
    # Init var to return
    noteSum = 0
    
    # For every pattern, split into line
    for pattern in patterns:
        pattern = pattern.split('\n')
        patternValue = 0
        
        # Check every horizontal line
        for i, p in enumerate(pattern[1:], start = 1):
            
            # If we found a reflection line, remember its value and break
            if get_differences(pattern, i) == differences:
                patternValue = i * 100
                break
            
        # Otherwise, do the same for the vertizal lines
        if patternValue == 0:
            
            columns = list(map(''.join, zip(*pattern)))
                   
            for i, p in enumerate(columns[1:], start = 1):
                
                if get_differences(columns, i) == differences:
                    patternValue += i
                    break
            
        # Add to the total
        noteSum += patternValue
        
    return noteSum

# Read and parse the input
f = open('input.txt', 'r')
patterns = f.read().split('\n\n')

# Compute the results
noteSum = get_pattern_value_sum(patterns)
noteSumSmudge = get_pattern_value_sum(patterns, 1)

# Print the results
print(f'The sum of notes is {noteSum}')
print(f'The som of notes with smudges on the mirrors is {noteSumSmudge}')