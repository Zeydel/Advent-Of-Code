import re

# Get the sum of mul operations in a string
def get_mul_sum(string):
    
    # Init as zero
    mul_sum = 0
    
    # For every match of the regex
    for match in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', string):
        
        # Get the matched string
        substring = match.group()
        
        # Remove 'mul(' and ')'
        substring = substring[4:-1]
        
        # Split into two numbers
        num1, num2 = substring.split(',')
        
        # Add their product to the sum
        mul_sum += int(num1) * int(num2)
        
    # Return the sum
    return mul_sum
        
# Get the list of strings where do() is active
def get_do_strings(string):
    
    # Split on do()
    do_strings = string.split('do()')
    
    # For every string, remove the part after the first don't()
    do_strings = [do_string.split('don\'t()')[0] for do_string in do_strings]
    
    # Return the list of strings
    return do_strings
    
# Open the file and read as one long string
file = open('input.txt', 'r')
string = file.read()

# Get the total sum of mul operations
mul_sum = get_mul_sum(string)

# Init var for second result
do_mul_sum = 0

# For every do() string, add the result of mul operations
for do_string in get_do_strings(string):
    
    do_mul_sum += get_mul_sum(do_string)

# Print the results
print(f'{mul_sum} is the sum of mul() operations')
print(f'{do_mul_sum} is the sum of mul() operations after do() operations')