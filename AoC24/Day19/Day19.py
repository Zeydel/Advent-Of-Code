# Parse the input into towels and targets
def parse(lines):
    
    towels = lines[0].split(', ')
    
    targets = lines[2:]
    
    return towels, targets

# Get the number of arrangements of twoels that can become the target
def get_number_of_arrangements(target, towels, memo_dict):
    
    # If there is nothing left to search for, return 1
    if len(target) == 0:
        return 1
    
    # If we already know the result, return it
    if target in memo_dict:
        return memo_dict[target]
    
    # Else init a var for the result
    possible = 0
    
    # For each towel
    for towel in towels:
        
        # If the towel matches the start of the towel
        if target.startswith(towel):
            
            # Recurse
            possible += get_number_of_arrangements(target[len(towel):], towels, memo_dict)
    
    # Add the result to the memoization dict
    memo_dict[target] = possible
    
    # Return the number of arrangements
    return possible
    
# Open input and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
towels, targets = parse(lines)

# Init var for the results
possible_targets = 0
possible_arrangements = 0

# Init a memoization dict
memo_dict = dict()

# For every target
for target in targets:
    
    # Get the number of possible arrangements
    arrangements = get_number_of_arrangements(target, towels, memo_dict)
    
    # If the result is not zero, add to the result vars
    if arrangements > 0:
        possible_targets += 1
        possible_arrangements += arrangements
        
# Print the results
print(f'{possible_targets} is the number of arrangements that are possible')
print(f'{possible_arrangements} is the total number of correct arrangements')