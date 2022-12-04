# Parse the list into list of tuples of sets
def parse(pairs):
    
    pairlist = []
    
    # For every pair
    for p in pairs:
        
        # Split it
        split = p.split(',')
        
        # Make sets of each of the ranges
        first = set(range(int(split[0].split('-')[0]), int(split[0].split('-')[1])+1))
        second = set(range(int(split[1].split('-')[0]), int(split[1].split('-')[1])+1))
        
        # Add to the list
        pairlist.append((first, second))
        
    return pairlist


# Read and parse the input
f = open('input.txt', 'r')
pairs = f.read().split('\n')

# Parse the input
pairs = parse(pairs)

# Init counters
subsetcount = 0
overlapcount = 0

# For every pair
for p in pairs:
    
    # If one is a subset of the other, increment
    if p[0].issubset(p[1]) or p[1].issubset(p[0]):
        subsetcount += 1
        
    # If the intersection has a size greater than 0, increment
    if p[0].intersection(p[1]):
        overlapcount += 1
    
# Print the results
print(f'There are {subsetcount} segments that fully contain another section')
print(f'There are {overlapcount} overlapping segments')