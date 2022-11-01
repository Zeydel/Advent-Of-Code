# Gets all combinations of containers that contain the target value
def getCombinations(sizes, target, containercount = 0):
    
    # If we het the target, add one to the corresponding value and return
    if target == 0:
        if containercount not in combinations:
            combinations[containercount] = 0
        combinations[containercount] += 1
        return
    
    # We have overshort the target. Return
    if target < 0:
        return
    
    # No more containers. Return
    if len(sizes) == 0:
        return
    
    # Get the number of combinations using the first container in the array
    getCombinations(sizes[1:], target-sizes[0], containercount + 1)
    
    # Get the number of combinations not using the first container in the
    # array
    getCombinations(sizes[1:], target, containercount)
    
    return combinations
    

# Read as set of numbers
f = open('input.txt', 'r')
sizes = sorted([int(s) for s in f.read().split('\n')])

# Get the number of combinations
combinations = dict()
getCombinations(sizes, 150)

# Print the result
print(f'The number of different combinations is {sum([combinations[c] for c in combinations])}')
print(f'The number of combinations using the minimum number of containers is {combinations[min(combinations.keys())]}')