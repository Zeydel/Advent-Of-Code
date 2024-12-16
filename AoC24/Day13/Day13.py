# Parse the input into tuples of arrays representing the sets of equations
def parse(lines):
    
    equation_pairs = []
    
    for i in range(0, len(lines), 4):
        
        line1 = lines[i]
        line2 = lines[i+1]
        line3 = lines[i+2]
        
        line1 = line1.split(': ')[1]
        line1 = line1.split(', ')
        line1 = [int(line1[0].split('+')[1]), int(line1[1].split('+')[1])]
        
        line2 = line2.split(': ')[1]
        line2 = line2.split(', ')
        line2 = [int(line2[0].split('+')[1]), int(line2[1].split('+')[1])]
        
        line3 = line3.split(': ')[1]
        line3 = line3.split(', ')
        line3 = [int(line3[0].split('=')[1]), int(line3[1].split('=')[1])]
        
        eq1 = [line1[0], line2[0], line3[0]]
        eq2 = [line1[1], line2[1], line3[1]]
        
        equation_pairs.append((eq1, eq2))
        
    return equation_pairs 

# Solve a pair of equations using Cramers rule
def solve_equations(equation_pair):
    
    # Get each equation
    eq1, eq2 = equation_pair
    
    # Get the determintans
    det = (eq1[0] * eq2[1]) - (eq2[0] * eq1[1])
    
    det_a = (eq1[2] * eq2[1]) - (eq2[2] * eq1[1])
    
    det_b = (eq1[0] * eq2[2]) - (eq2[0] * eq1[2])
    
    # Find reuslts
    a = det_a/det
    
    b = det_b/det
    
    # We are only interested in integer results
    if a.is_integer() and b.is_integer():
        return (int(a), int(b))
    
    return (-1, -1)

# Update equations by adding 10000000000000 to the rhs
def update_equations(equations):
    
    updated_equations = []
    
    for eq1, eq2 in equations:
        
        eq1[2] += 10000000000000
        eq2[2] += 10000000000000
        
        updated_equations.append((eq1, eq2))
        
    return updated_equations
        
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Get the list of equations
equations = parse(lines)

# Init var for the result
tokens = 0

# For every equation
for equation in equations:
    
    # Solve it
    a, b = solve_equations(equation)
    
    # If it has an integer solution, add the tokens needed to it
    if a != -1 and b != -1:
        tokens += (3*a) + b
        
# Do the same thing with the updated equations
tokens_updated = 0
equations = update_equations(equations)

for equation in equations:
    
    a, b = solve_equations(equation)
    
    if a != -1 and b != -1:
        tokens_updated += (3*a) + b
        
print(f'{tokens} tokens are needed to get the prizes')
print(f'{tokens_updated} tokens are needed to get the prizes on the updated locations')