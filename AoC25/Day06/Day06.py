import math

# Parse the input into a list of lists of numbers and their operators
def parse(lines):
    
    length = len(lines[0].split())
    
    formulas = [[] for _ in range(length)]
    
    for line in lines:
        
        split = line.split()
        
        for i, num in enumerate(split):
            
            if num[0].isdigit():
                formulas[i].append(int(num))
            else:
                formulas[i].append(num)
                
    return formulas

# Parse the input into a list of lists of numbers and their operators
# where the numbers are read vertically
def parse_vertical(lines):
    
    formulas = []
    
    sign_indices = []
    
    for i in range(len(lines[-1])):
        
        if lines[-1][i] != ' ':
            sign_indices.append(i)
            
    sign_indices.append(len(lines[-1])+1)
    
    for i in range(len(sign_indices[:-1])):
        
        formula = []
        
        start = sign_indices[i]
        end = sign_indices[i+1]-1
        
        for j in range(start, end):
            
            number = ''
            
            for k in range(0, len(lines[:-1])):
                
                if lines[k][j] != ' ':
                    number += lines[k][j]
                 
            formula.append(int(number))
            
        formula.append(lines[-1][sign_indices[i]])
        
        formulas.append(formula)
        
    return formulas
    
# Given a formula, get the sum or product depending of the sign
def calculate_formula(formula):
    
    if formula[-1] == '+':
        return sum(formula[:-1])
    elif formula[-1]  == '*':
        return math.prod(formula[:-1]) 

# Get the sum of results of every formula
def get_formula_sum(formulas):
    
    formula_sum = 0
    
    for f in formulas:
        formula_sum += calculate_formula(f)
        
    return formula_sum

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line for line in file.readlines()]

# Parse the input both ways
formulas = parse(lines)
vertical_formulas = parse_vertical(lines)

# Calculate the results
formula_sum = get_formula_sum(formulas)
formula_sum_vertical = get_formula_sum(vertical_formulas)

# Print the results
print(f'The sum of results of all problems is {formula_sum}')
print(f'The sum of results of all problems is {formula_sum_vertical}')