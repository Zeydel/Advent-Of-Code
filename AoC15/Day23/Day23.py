# Parses the input to an array of functions. Done to avoid
# parsing strings every time we have to call a function
def parse(strings):
    
    # Initally empty list of functions
    functions = []
    
    # For every string
    for s in strings:
        # Split it, and do some parsing
        split = s.split(' ')
        
        if len(split) == 2:
            r = split[1]
        else:
            r = split[1][:-1]
            v = int(split[2])
        
        # Create a function according to the operation
        if split[0] == 'hlf':
            # I use default parameters as these are evaluated as the 
            # function is created. If i simply used the 'r' and 'v'
            # variables in the functions, these would only be evaluated
            # when the function was called and would contain the wrong value
            def hlf(r=r):
                registers[r] //= 2
                registers['p'] += 1
            functions.append(hlf)
        elif split[0] == 'tpl':
            r = split[1]
            def tpl(r=r):
                registers[r] *= 3
                registers['p'] += 1
            functions.append(tpl)
        elif split[0] == 'inc':
            def inc(r=r):
                registers[r] += 1
                registers['p'] += 1
            functions.append(inc)
        elif split[0] == 'jmp':
            def jmp(v=int(r)):
                registers['p'] += v
            functions.append(jmp)
        elif split[0] == 'jie':
            def jie(r=r, v=v):
                if registers[r] % 2 == 0:
                    registers['p'] += v
                else: registers['p'] += 1
            functions.append(jie)
        elif split[0] == 'jio':
            def jio(r=r, v=v):
                if registers[r] == 1:
                    registers['p'] += v
                else: registers['p'] += 1
            functions.append(jio)
                
    return functions
        

## Read input and parse
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Parse the strings into a list of functions
functions = parse(strings)

# Define the registers and the starting values
registers = {
    'a' : 0,
    'b' : 0,
    'p' : 0
    }

# Run the code untill p is out of bounds
while(registers['p'] < len(functions)):
    # Run the p'th function
    functions[registers['p']]()
    
# Save the result from round 1
roundOne = registers['b']

# Reinit the registers
registers = {
    'a' : 1,
    'b' : 0,
    'p' : 0
    }

# Do the same thing again
while(registers['p'] < len(functions)):
    functions[registers['p']]()

roundTwo = registers['b']

# Print the results
print(f'After round one, the value in register b is {roundOne}')
print(f'After round two, the value in register b is {roundTwo}')
