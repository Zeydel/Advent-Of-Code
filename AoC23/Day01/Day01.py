import re

# Function to get sum of calibration values
def get_calibration_sum(values, numbers):
    
    # Init the sum
    cal_sum = 0
    
    # Create a regex with lookback to handle overlapping numbers
    regex = "(?=(" + "|".join(numbers) + "))"
    
    # For every value in list
    for v in values:
        
        # Find all matches
        matches = re.findall(regex, v)
        
        # Handle the first found digit
        if len(matches[0]) == 1:
            first_digit = matches[0]
        else:
            first_digit = number_map[matches[0]]
            
        # Handle the last found digit
        if len(matches[-1]) == 1:
            last_digit = matches[-1]
        else:
            last_digit = number_map[matches[-1]]
        
        # Append the digits, convert to integer, add to sum
        cal_sum += int(first_digit + last_digit)
        
    # Return the sum
    return cal_sum
    
# Map digits to their numerical value
number_map = {'one': '1',
              'two': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9'}

# Read and parse the input
f = open('input.txt', 'r')
values = f.read().split('\n')

# Degine lists of digits
digits = list(number_map.values())
alphanumeric_digits = list(number_map) + list(number_map.values())

# Print the results
print(f'The numeric calibration sum is {get_calibration_sum(values, digits)}')
print(f'The alphanumeric calibration sum is {get_calibration_sum(values, alphanumeric_digits)}')