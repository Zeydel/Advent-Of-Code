# Function to compute the differences between each pair of number in list
def get_differences(numbers):
    
    return [numbers[i+1] - numbers[i] for i, n in enumerate(numbers[:-1])]

# Function to extrapolae the next number, given a computed stack of numbers
def get_next_number(stack):
    
    # Reverse the lsit
    stack = list(reversed(stack))
    
    # Append a zero
    stack[0].append(0)
    
    # For every non-zero line, compute the next number
    for i, n in enumerate(stack[1:]):
        
        stack[i+1].append(stack[i][-1] + n[-1])
        
    # Return the final number of the first line (final line, since its reversed)
    return stack[-1][-1]
            
# Function to extrapolate the previous number, using the same logic as above
def get_prev_number(stack):
    stack = list(reversed(stack))
    stack[0].insert(0,0)

    for i, n in enumerate(stack[1:]):
        
        stack[i+1].insert(0, n[0] - stack[i][0])
        
    return stack[-1][0]

# Read and parse the input
f = open('input.txt', 'r')
report = f.read().split('\n')

# Parse the input as lists of integers
report  = [[int(i) for i in numbers.split()] for numbers in report]

# Init vars for results
next_number_sum = 0
prev_number_sum = 0

# For every input line
for r in report:
    
    # Init stack as just the input
    stack = [r]
    
    # While we dont have a line of zeroes, compute the next line and add it to the stack
    while not all([i == 0 for i in r]):
        
        r = get_differences(r)
        stack.append(r)
        
    # Compute next and previous numbers, and add them to the results
    next_number_sum += get_next_number(stack)
    prev_number_sum += get_prev_number(stack)

# Compute the results
print(f'The sum of extrapolated next numbers is {next_number_sum}')
print(f'The sum of extrapolated previous numbers is {prev_number_sum}')