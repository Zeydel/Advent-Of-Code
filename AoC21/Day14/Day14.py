# Function to perform one iteration of the expansion
def expand_counts(counts, expansions):
    
    # Create new dict with same keys as old one
    new_counts = dict()
    for k in counts.keys():
        new_counts[k] = 0
        
    # For every key
    for k in counts.keys():
    
        # Get the two new strings created from the expansion
        ex_1 = k[0] + expansions[k]
        ex_2 = expansions[k] + k[1]

        # Add the old count of k to the count of the newly created strings
        new_counts[ex_1] += counts[k]
        new_counts[ex_2] += counts[k]
    
    # Return the new string
    return new_counts
        
# Get the count of a specific character based on the counts
def get_character_count(character, counts, template):
    
    # Init as zero
    count = 0
    
    # For every count
    for c in counts:
        
        # If c is character twice, add count times two
        if c == character + character:
            count += counts[c] * 2
            
        # Else if character is in c, add the count
        elif character in c:
            count += counts[c]
            
    # If the character is at the start or end, increment the count
    if character == template[0] or character == template[-1]:
        count += 1
        
    # Divide by two. Count should always be even here
    return int(count / 2)

# Get the result to be printed
def get_difference_between_most_and_least_common(counts):
    
    # Get the set of chars in counts
    chars = set(''.join([k for k in counts]))

    # Init results
    max_count = 0
    min_count = float('inf')
    
    # Count each char. Update max or min if necessary
    for c in chars:
    
        character_count = get_character_count(c, counts, template)

        if character_count > max_count:
            max_count = character_count
            
        if character_count < min_count:
            min_count = character_count
            
    # Return the difference
    return max_count - min_count


# Open input and read as lines
f = open('input.txt', 'r')
lines = f.read().split('\n')

# Template is the first line
template = lines[0]

# Create dicts for expansions for counts
expansions = dict()
counts = dict()

# For all remaining lines, add the expansion, and add a count of zero
for l in lines[2:]:
    expansions[l.split(' -> ')[0]] = l.split(' -> ')[1]
    counts[l.split(' -> ')[0]] = 0
    
# Go through template and count pairs.
for p in zip(template[:-1], template[1:]):
    counts[''.join(p)] += 1

# Perform expansion 10 times and save the result
for i in range(10):
    counts = expand_counts(counts, expansions)

difference_after_10 = get_difference_between_most_and_least_common(counts)

# Perform expansion 30 more times and save the result
for i in range(30):
    counts = expand_counts(counts, expansions)

difference_after_40 = get_difference_between_most_and_least_common(counts)

# Print the results
print('After 10 iterations, the difference between the most and least common character is ' + str(difference_after_10))
print('After 40 iterations, the difference between the most and least common character is ' + str(difference_after_40))
