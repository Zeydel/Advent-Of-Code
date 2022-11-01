# Parses the input into a dict of dicts
def parse(strings):
    
    # Init empty dict
    sues = dict()
    
    # For every string
    for s in strings:
        
        # Strip the unimportant parts
        s = s.lstrip('Sue ')
        split = s.split(' ')
        split = [s.strip(':').strip(',') for s in split]
        
        # Every key is the number of the sue. The inner dicts is the names
        # and values of the properties
        props = dict([(split[i], int((split[i+1]))) for i in range(1,6,2)])
        
        sues[int(split[0])] = props
        
    # Return the sues
    return sues

# Function to filter sues based on a scan
def filterSues(sues, scan):
    
    # Assume all sues live up to the scan
    rightSues = list(sues.keys())
    
    # For every sue
    for s in sues:
        # For every property that we know about the sue
        for p in sues[s]:
            
            # If the sue does not match the scan, remove her
            if sues[s][p] != scan[p]:
                rightSues.remove(s)
                break
        
    # Return the right sue(s) (hopefully just one)
    if len(rightSues) == 1:
        return rightSues[0]
    else:
        return rightSues

# Function to filter sues based on scan, using the nonexact values
def filterSuesNonexact(sues, scan):
    
    # Assume all sues live up to the scan
    rightSues = list(sues.keys())
    
    # For every sue
    for s in sues:
        # For every property that we know about the sue
        for p in sues[s]:
            # If it a cat or tree, check that the sue has more than the scan
            # otherwise remove
            if p in ('cats', 'trees'):
                if sues[s][p] <= scan[p]:
                    rightSues.remove(s)
                    break
            # If it is a pomeranian or goldfish, check that the sue has fewer
            # than the one in the scan. Otherwise remove
            elif p in ('pomeranians', 'goldfish'):
                if sues[s][p] >= scan[p]:
                    rightSues.remove(s)
                    break
            # Else just check that the property matches
            elif sues[s][p] != scan[p]:
                rightSues.remove(s)
                break
            
    # Return the right sue(s) (hopefully still just one)
    if len(rightSues) == 1:
        return rightSues[0]
    else:
        return rightSues

# Read as strings
f = open('input.txt', 'r')
strings = set(f.read().split('\n'))

# The scan
scan = set([
        'children: 3',
        'cats: 7',
        'samoyeds: 2',
        'pomeranians: 3',
        'akitas: 0',
        'vizslas: 0',
        'goldfish: 5',
        'trees: 3',
        'cars: 2',
        'perfumes: 1' 
        ])
# Transform scan into a dict
scan = dict([(sp.split(': ')[0], int(sp.split(' ')[1])) for sp in scan])

# Parse the input
sues = parse(strings)

# Print the results
print(f'The right Sue is Sue {filterSues(sues, scan)}')
print(f'The actual right Sue is Sue {filterSuesNonexact(sues, scan)}')