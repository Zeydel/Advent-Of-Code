# Function to check the surroundings of a number for symbels
def check_surroundings(left_index, right_index, row, number):
    
    # Check around the number, but bound by schematic size
    for i in range(max(row-1, 0), min(row+2, len(schematic))):
        for j in range(max(left_index-1, 0), min(right_index+2, len(schematic[0]))):
            
            # If the character is not a . or a number, we should return true
            if schematic[i][j] != '.' and not schematic[i][j].isnumeric():
                
                # If the character is a *, remember its position and save its number
                if schematic[i][j] =='*':
                    if (i,j) not in gears:
                        gears[(i,j)] = []
                    gears[(i,j)].append(int(number))
                
                return True
            
    # If we haven't found any symbols, return false
    return False


# Read and parse the input
f = open('input.txt', 'r')
schematic = f.read().split('\n')

# Init an empty list of gears
gears = {}

# Vars for the results
part_number_sum = 0
gear_ratio_sum = 0

# Go through every line
for i, line in enumerate(schematic):
    
    # Init some variables to keep track of found numbers
    left_index = -1
    right_index = -1
    number = ''
    
    # Go through every character
    for j, char in enumerate(line):
        
        # If we find a number
        if char.isnumeric():
            
            # Remember its starting position
            if number == '':
                left_index = j
                
            # Remember the number and its end position
            number += char
            right_index = j
        
        # If we have a number remembered and we stop finding numbers
        if not char.isnumeric() and len(number) > 0:
            
            # If it is surrounded by a symbol add it to the result
            if check_surroundings(left_index, right_index, i, number):
                part_number_sum += int(number)
                
            # Reset the number
            number = ''
            
    # If we reach the end of a line and have a number saved, do the check again
    if len(number) > 0:
        if check_surroundings(left_index, right_index, i, number):
            part_number_sum += int(number)
                
        number = ''
            
# Go through the list of found gears
for g in gears:
    
    # If they are surrounded by two numbers, add the product of its numbers
    if len(gears[g]) == 2:
        gear_ratio_sum += gears[g][0] * gears[g][1] 

# Print the results
print(f'The sum of part numbers is {part_number_sum}')
print(f'The sum of gear ratios is {gear_ratio_sum}')