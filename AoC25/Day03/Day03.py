# Given a bank and a battery length, compute the optimal
# batteries to turn on
def get_best_output(bank, length):
    
    # Empty output
    output = ''
    
    # Start at the beginning
    start = 0
    
    # For every i in the length, going backwards
    for i in range(length, 0, -1):
        
        # Assume the best index is the first one
        best_index = start
        
        # For every battery from the start, to where we can go
        # and still have batteries left for the rest of the iterations
        for b in range(start, (len(bank)+1)-i):
            
            # If current battery is better than best, overwrite it
            if bank[b] > bank[best_index]:
                best_index = b
                
        # Add the best battery to the output
        output += bank[best_index]
        
        # Define new start point
        start = best_index + 1
        
    # Return answer as int
    return int(output)

# Sum all best outputs
def get_best_output_sum(banks, length):
    
    output_sum = 0
    
    for bank in banks:
        
        output_sum += get_best_output(bank, length)
        
    return output_sum

# Open file and read as lines
file = open('input.txt', 'r')
banks = [line.strip() for line in file.readlines()]

# Define problem variables
short_battery = 2
long_battery = 12

# Compute the best total outputs
best_output = get_best_output_sum(banks, short_battery)
best_output_long_battery = get_best_output_sum(banks, long_battery)

# Print the results
print(f'The best output sum with short batteries is {best_output}')
print(f'The best output sum with long batteries is {best_output_long_battery}')
