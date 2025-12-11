from itertools import combinations
from scipy.optimize import linprog
import numpy as np

# Parse the input into machines
def parse(lines):
    
    machines = []
    
    for line in lines:
        
        parts = line.split()
        
        target = parts[0][1:-1]
        
        target = [True if char == '#' else False for char in target]
        
        joltage = parts[-1]
        
        joltage = joltage[1:-1].split(',')
        
        joltage = [int(j) for j in joltage]
        
        buttons = parts[1:-1]
        
        button_sets = []
        
        for button in buttons:
            
            button = button[1:-1]
            
            button_sets.append([int(b) for b in button.split(',')])
            
        machines.append((target, button_sets, joltage))
        
    return machines
     
# Check wether a combination of button presses yeld the correct result    
def is_combination_correct(combination, buttons, target):
    
    attempt = [False] * len(target)
    
    for button in combination:
        
        for connection in button:
            
            attempt[connection] = not attempt[connection]
            
    return attempt == target
    
# Get optimal button count to configure indicator lights for a machine
def get_optimal_button_count(machine):
    
    # Get problems variables for machine
    target, buttons, _ = machine
    
    # Start size at zero, and go until it is the length of the list of buttons
    size = 0
     
    while size < len(buttons):
                
        size += 1
        
        # For all combinations of given size
        for combination in combinations(buttons, size):
        
            # If combination works, return size
            if is_combination_correct(combination, buttons, target):
                return size
            
    # If we get here, the indicator lights will never turn on
    return float('inf')

# Get optimal button count to configure joltage by integer programming
def get_optimal_button_count_joltage(machine):
    
    # Get variables
    _, buttons, target = machine
    
    # Get funtion to minimize as sum of button presses
    c = [1] * len(buttons)
    
    # Get the A array
    A = []
    
    for button in buttons:
        
        a_row = [0] * len(target)
        
        for connection in button:
            
            a_row[connection] = 1
            
        A.append(a_row)
            
    # Solve by integer progamming
    result = linprog(c, A_eq=np.transpose(A), b_eq=target, integrality=1)
        
    # Return sum of presses on each button
    return sum([round(x) for x in result.x])

# Solve both problems in one pass of the problem array
def get_optimal_button_count_sum(machines):
    
    # Init answers as zero
    button_count_sum = 0
    button_count_sum_joltage = 0
    
    # For every machine, add solutions to problems
    for machine in machines:
         
        button_count_sum += get_optimal_button_count(machine)
        button_count_sum_joltage += get_optimal_button_count_joltage(machine)
                        
    # Return the solutions
    return button_count_sum, button_count_sum_joltage


# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
machines = parse(lines)

# Solve the problems
button_count_sum, button_count_sum_joltage = get_optimal_button_count_sum(machines)

# Print the results
print(f'{button_count_sum} presse are required to configure the indicator lights')
print(f'{button_count_sum_joltage} presse are required to configure the joltage levels')