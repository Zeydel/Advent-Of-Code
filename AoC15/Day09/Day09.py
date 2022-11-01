# We need itertools to generate permutations
import itertools

# Function to parse the input into a dictionary
def parse(strings):
    
    # Initially empty
    dists = {}

    # For every line
    for s in strings:
        
        # Split the string
        split = s.split(' ')
        
        # Add both permutations of cities to the dict along with the distance 
        dists[(split[0],split[2])] = int(split[4])
        dists[(split[2],split[0])] = int(split[4])
        
    # Return the dict
    return dists

# Function to get both the shortest and longest distance
def getShortestsAndLongestDistance(cities, dists):
    
    # Init vars to store shortest and longest distance
    shortestDist = float('inf')
    longestDist = float('-inf')
    
    # For every permutation (onlu 5040 different. Thats why we can bruteforce)
    for p in itertools.permutations(cities):
        dist = 0
        
        # For every pair of cities
        for i in range(len(p)-1):
            
            # Add their distance to the dist
            dist += dists[(p[i],p[i+1])]
        
        # If we have found a new shortest or longest, store it
        if dist < shortestDist:
            shortestDist = dist
        if dist > longestDist:
            longestDist = dist
            
    # Return the results
    return (shortestDist, longestDist)


# Read as strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Parse the strings
dists = parse(strings)

# Get all the lists from the input
cities = set([s.split(' ')[0] for s in strings])
cities = cities.union(set([s.split(' ')[2] for s in strings]))

# Compute the results
results = getShortestsAndLongestDistance(cities, dists)

print(f'The shortest distance is {results[0]}')
print(f'The longest distance is {results[1]}')