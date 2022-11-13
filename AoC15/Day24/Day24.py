# Imports to do things quicker
from itertools import combinations
import operator
from functools import reduce

# Function to check if it is possible divide the presents into subsets that
# all have the specified sum
def isDivisionPossible(presents, subset, size):
    
    # Rmove the presents that we already know to sum to the sum
    presents = [p for p in presents if p not in subset]
    
    # For every possible lenght of combination
    for i in range(len(presents) + 1):
        # Create all the combinations of that length
        for subset in combinations(presents, i):
            # Check if the sum is equal to the desired sum AND either the remaining presents also make up the sum
            #                                              OR  the remaining presents can be divided as to make up the sum
            if sum(subset) == size and (sum(presents) == 2*size or isDivisionPossible(presents, subset, size)):
                return True
    # Return false if we haven't found anything
    return False

# Get all possible smallest subsets that add up to the given sum
def getSubsetsOfSize(presents, size):
    
    # Init empty list
    subsets = []
    
    # For all possible subset length
    for i in range(len(presents) + 1):
        # If we have found smaller subsets, break the loop
        if len(subsets) > 0:
            break
        # For every combination of the given length
        for subset in combinations(presents, i):
            # Check that the presents sum up to the desired number, and that
            # we can divide the remaining presents into sets of that number
            if sum(subset) == size and isDivisionPossible(presents, subset, size):
               subsets.append(subset)

    return subsets

# Finds the subset with the smallest Quantum entanglement
def findBestSubset(subsets):
    
    bestQe = float('inf')
    
    # For every subset
    for s in subsets:
        
        # If its quantum entanglement is better than the current, save it
        if reduce(operator.mul, s) < bestQe:
            bestQe = reduce(operator.mul, s)
    return bestQe

## Read input and parse
f = open('input.txt', 'r')
presents = [int(i) for i in f.read().split('\n')]

# Find the subsets that add up to the desired value
subsetsThreeCompartments = getSubsetsOfSize(presents, sum(presents)//3)
subsetsFourCompartments = getSubsetsOfSize(presents, sum(presents)//4)

# Print the results
print(f'The best quantum entanglement for three compartments is {findBestSubset(subsetsThreeCompartments)}')
print(f'The best quantum entanglement for four compartments is {findBestSubset(subsetsFourCompartments)}')