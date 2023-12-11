# Function to compute new galaxy locations given map of stars and expansion factors
def expandSpace(starMap, galaxies, expansionFactor):
    
    # We need to keep track of offset to not expand too much
    offset = 0
    
    # For every line, check if it is emptyu
    for i, line in enumerate(starMap):
        if all([c == '.' for c in line]):
            
            # If it is, go through all galaxies and compute new x coordinate
            for j, g in enumerate(galaxies):
                if g[0] > i + offset:
                    galaxies[j] = (g[0] + expansionFactor - 1, g[1])
                    
            # Add to the offset
            offset += expansionFactor - 1
               
    # The same as above but for columns
    offset = 0
    # Use some python hackines to get columns
    for i, column in enumerate(list(map(''.join, zip(*starMap)))):
       if all([c == '.' for c in column]):
           for j, g in enumerate(galaxies):
               if g[1] > i + offset:
                   galaxies[j] = (g[0], g[1] + expansionFactor - 1)
                   
           offset += expansionFactor - 1
                    
    return galaxies

# Go through every character and find galaxies
def find_galaxies(starMap):
    
    galaxies = []
    
    for x, line in enumerate(starMap):
        for y, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
                
    return galaxies

# Read and parse the input
f = open('input.txt', 'r')
starMap = f.read().split('\n')

# Find galaxies and compute their expanded locations
galaxies = find_galaxies(starMap)
galaxies = expandSpace(starMap, galaxies, 2)

# Compute all distances
distanceSumFactor2 = 0

for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        distanceSumFactor2 += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
        
# The same as above but for the new expansion factor
galaxies = find_galaxies(starMap)
galaxies = expandSpace(starMap, galaxies, 1000000)

distanceSumFactor1000000 = 0

for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        distanceSumFactor1000000 += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

# Print the results
print(f'The sum of distances between galaxies with expansion factor 2 is {distanceSumFactor2}')
print(f'The sum of distances between galaxies with expansion factor 1000000 is {distanceSumFactor1000000}')