# Check if we should even bother recursing
def should_recurse(springs, groups):
    
    # If there is not enough room left to put remaining springs return False
    if sum([1 for c in springs if c in ('#', '?')]) < sum(groups):
        return False
    
    # If the list if too short, return false
    if len(springs) < sum(groups) + (len(groups)-1):
        return False
    
    # If there are too many springs already return false
    if sum([1 for c in springs if c == '#']) > sum(groups):
        return False
        
    # Otherwise, return True
    return True

# Check if we can place a set of springs on the list, starting from some index
def can_place(springs, number, index):
    
    # If there is a . at any point in the sequence, return false
    if any([c == '.' for c in springs[index:index+number]]):
        return False
    
    # If there is a # just before and we are not at the start, return False
    if index != 0 and springs[index-1] == '#':
        return False
    
    # If we exceed the bound, return False
    if index + number > len(springs):
        return False
    
    # If there is a # at the end, return False
    if springs[index+number] == '#':
        return False
    
    # Otherwise return ture
    return True

# Function to get the number of ways we can place a group of springs
def get_number_of_placements_for_group(springs, number):
    
    # Counter
    placements = 0
    
    # Split into groups, and count groups with #
    splitSprings = springs.replace('.', ' ').split()
    withSpring = []
    for s in splitSprings:
        if '#' in s:
            withSpring.append(s)
    
    # If multiple groups has #, we cannot place the springs
    if len(withSpring) > 1:
        return placements
    
    # If zero groups has it, we can calculate the number of ways to place springs
    if len(withSpring) == 0:
        for s in splitSprings:
            if len(s) >= number:
                placements += len(s) - (number-1)
    
        return placements
    
    # If one group has it, we count the ways we can place the springs
    withSpring = withSpring[0]
    i = 0
    while i + number <= len(withSpring):
        replaced = withSpring[:i] + '#'*number + withSpring[i+number:]
        if sum([1 for c in replaced if c == '#']) == number:
            placements += 1
            
        i += 1
        
    # Return the calculated number
    return placements
            
        
# Recursvive function to get number of spring arrangements
def get_number_of_arrangements(springs, groups):
            
    # Counter
    arrangementCount = 0
    
    # If there isnt any groups, we return 1 if there is no springs in the string
    if len(groups) == 0:
        if any([c == '#' for c in springs]):
            return 0
        else:
            return 1
    
    # IF there one group left, we calculate the number of placements seperately
    if len(groups) == 1:
        return get_number_of_placements_for_group(springs, groups[0])
    
    # Find the middle group    
    middleGroup = groups[len(groups)//2]
    
    # For all possible placements of the middle group
    i = 0
    while i + middleGroup <= len(springs):
        
        # IF the group can be placed at this index
        if can_place(springs, middleGroup, i):
                        
            # Compute the new strings
            left_replaced = springs[:i-1] + '.'
            right_replaced = '.' + springs[i+middleGroup+1:]
            
            # Check if we should even bother recursing
            if should_recurse(left_replaced, groups[:len(groups)//2]) and should_recurse(right_replaced, groups[(len(groups)//2)+1:]):
                
                # Compute the number of placements in the left substring
                leftArrangements = get_number_of_arrangements(left_replaced, groups[:len(groups)//2])
                
                # If any, repeat for the right. Add the product of these two numbers to the result
                if leftArrangements > 0:
                    rightArrangements = get_number_of_arrangements(right_replaced, groups[(len(groups)//2)+1:])
                    arrangementCount += leftArrangements * rightArrangements
            
        i += 1
            
    # Return the count
    return arrangementCount
            
            

# Read and parse the input
f = open('input.txt', 'r')
records = f.read().split('\n')

springList = []
groupList = []

# Parse the input
for r in records:
    springLine, groupLine = r.split()
    springList.append(springLine)
    groupList.append([int(n) for n in groupLine.split(',')])

# Result vars    
arrangementSum = 0
foldedArrangementSum = 0

# For every spring in list, calculate number of placements and sum
for i, s in enumerate(springList):
    arrangementSum += get_number_of_arrangements('.' + s + '.', groupList[i])
    
# Repeat for the folded instructions
for i, s in enumerate(springList):
    foldedSprings = '?'.join([s for i in range(5)])
    foldedGroups = groupList[i]*5
    foldedArrangementSum += get_number_of_arrangements('.' + foldedSprings + '.', foldedGroups)
    
print(f'There are {arrangementSum} different possible arrangements')
print(f'There are {foldedArrangementSum} different possible arrangements, using the folded instructions')
# 227119854665793 too high