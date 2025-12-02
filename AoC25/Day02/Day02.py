# Parse the input into a list of ranges
def parse(line):
    
    ranges = []
    
    for r in line.split(','):
        
        start, end = r.split('-')
        
        ranges.append((int(start), int(end)))
        
    return ranges

# Get the sum of invalid ids
def get_invalid_id_sum(ranges):
    
    # Init as zero
    invalid_id_sum = 0
    
    # For every range
    for r_start, r_end in ranges:
        
        # For every number in the range
        for i in range(r_start, r_end+1):
            
            # Turn the number to a string
            i_str = str(i)
            
            # If the string is odd length, continue
            if len(i_str) % 2 == 1:
                continue
            
            # Split into halves
            first_half = i_str[:len(i_str) // 2]
            second_half = i_str[(len(i_str) // 2):]
            
            # If the first hald equals the second, add to sum
            if first_half == second_half:
                invalid_id_sum += i
                
    # Return sum
    return invalid_id_sum

def get_invalid_id_sum_length_invariant(ranges):
    
    # Init as zero
    invalid_id_sum = 0
    
    # For every range
    for r_start, r_end in ranges:
        
        # For every number in the range
        for i in range(r_start, r_end+1):
                        
            # Turn the number to a string
            i_str = str(i)
                
            # For every possible length that we can repeat
            for l in range(1, (len(i_str) // 2) + 1):
            
                # If the string not divisible by the length, continue
                if len(i_str) % l != 0:
                    continue
                
                # Split into strings of length l
                splits = [i_str[(l*i):l*(i+1)] for i in range(len(i_str) // l)]
                
                # If the first hald equals the second, add to sum
                if len(set(splits)) == 1:
                    invalid_id_sum += i
                    
                    # Stop checking
                    break
                
    # Return sum
    return invalid_id_sum


# Open file and read as lines
file = open('input.txt', 'r')
lines = file.readline().strip()

# Parse the input
ranges = parse(lines)

# Compute the results
invalid_id_sum = get_invalid_id_sum(ranges)
invalid_id_sum_length_invariant = get_invalid_id_sum_length_invariant(ranges)

# Print the results
print(f'The sum of invalid ids is {invalid_id_sum}')
print(f'The sum of invalid ids of invariant repeating length is {invalid_id_sum_length_invariant}')