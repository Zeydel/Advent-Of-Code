# Makes stuff a lot easier
from itertools import permutations

# Parses the list of strings into a dictionary
def parse(strings):
    
    # Init empty dict
    prefs = {}
    
    # For every line
    for s in strings:
        
        # Split the string
        split = s.split()
        
        # Find out the change in happinesss
        happiness = int(split[3])
        if split[2] == 'lose':
            happiness *= -1
            
        # Add the relation to the dict
        prefs[(split[0],split[10][0:-1])] = happiness
        
    return prefs
        
# Function for getting a happiness score given a permutation
def getScore(prefs, perm):
    
    # Initially zero
    score = 0
    
    # Add scpers for the first person
    score += prefs[(perm[0], perm[-1])]
    score += prefs[(perm[0], perm[1])]
    
    # Add scores for all the people in the middle
    for i in range(1, len(perm)-1):
        score += prefs[(perm[i], perm[i-1])]
        score += prefs[(perm[i], perm[i+1])]
        
    # And for the last person
    score += prefs[(perm[-1], perm[-2])]
    score += prefs[(perm[-1], perm[0])]
    
    return score
    
# Function to find the best score
def getBestScore(prefs, names):
    
    # Start with a score of 0 (we assume that the best score is over 0)
    bestScore = 0 
    
    # For every permutation
    for p in permutations(names):
        
        # Compute a score
        score = getScore(prefs, p)
        
        # If it is a new best score, save it.
        if score > bestScore:
            bestScore = score
            
    # Return the best score
    return bestScore

# Read as strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Get the neccessary info out of the input
prefs = parse(strings)
names = set([s.split()[0] for s in strings])

# Find the best score
bestScore = getBestScore(prefs, names)

# Thats me :)
me = 'me'

# Add me to all pairings
for n in names:
    prefs[me, n] = 0
    prefs[n, me] = 0

# Add me to the set of names
names.add(me)

# Recompute the best score
newBestScore = getBestScore(prefs, names)

print(f'The best score is {bestScore}')
print(f'The best score where i am also at the table is {newBestScore}')