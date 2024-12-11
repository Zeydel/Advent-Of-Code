# Break down each line into the target value and a list of numbers
def parse(lines):
    
    equations = []
    
    for line in lines:
        
        split_line = line.split(':')
        
        target = int(split_line[0])
        
        numbers = [int(num) for num in split_line[1].split()]
        
        equations.append((target, numbers))
        
    return equations
    
# Find out if it is possible to get to the target using a list of numbers
def is_possible(target, numbers):
    
    # If we are at the last number, and we have reached the target, return true
    if len(numbers) == 1 and numbers[0] == target:
        return True
    # If we are the last number and we have not reached the target, return false
    elif len(numbers) == 1:
        return False
    
    # Numbers will only grow. If we are bigger than the target, return false
    if numbers[0] > target:
        return False
    
    # Get the sum and product of the first two numbers
    add_result = numbers[0] + numbers[1]
    mul_results = numbers[0] * numbers[1]
    
    # Replace the first two numbers of the list with the sum and product and recurse
    return is_possible(target, [add_result] + numbers[2:]) or is_possible(target, [mul_results] + numbers[2:])
    
# Same as above, but include concat action
def is_possible_concat(target, numbers):
    
    if len(numbers) == 1 and numbers[0] == target:
        return True
    elif len(numbers) == 1:
        return False
    
    if numbers[0] > target:
        return False
    
    add_result = numbers[0] + numbers[1]
    mul_results = numbers[0] * numbers[1]
    concat_result = int(str(numbers[0]) + str(numbers[1]))
    
    return is_possible_concat(target, [add_result] + numbers[2:]) or is_possible_concat(target, [mul_results] + numbers[2:]) or is_possible_concat(target, [concat_result] + numbers[2:])

# Open file and read as list of lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the equations
equations = parse(lines)

# Init vars for results
possible_sum = 0
concat_possible_sum = 0

# For every equation
for target, numbers in equations:
    
    # Check if it is possible to get the result using all three actions
    if is_possible_concat(target, numbers):
        concat_possible_sum += target

        # Check if it is also possible to get the result using only addition and multiplying
        if is_possible(target, numbers):
            possible_sum += target

# Print the results
print(f'{possible_sum} is the sum of targets that can be reached using addition and multiplication')
print(f'{concat_possible_sum} is the sum of targets that can be reached using addition, multiplication, and concatonation')