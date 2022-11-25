# Parse the instructions into a list of functions
def parse(instruction):

    # Initially empty
    functions = []    

    # For every insrtuction
    for i in instructions:
        
        # Split it and parse is
        split = i.split()
        if len(split) == 3:
            x, y = split[1], split[2]
        else:
            x = split[1]
            
        # For every type of operations, create a function to do it
        # I use default parameters as they are evaluated when the
        # function is created an not when it is run. This way i end
        # up with len(instructions) distinct functions with their
        # own parameters
        if split[0] == 'cpy':
            def cpy(x=x, y=y):
                registers[y] = int(x) if x.isnumeric() else registers[x]
                registers['p'] += 1
            functions.append(cpy)
        elif split[0] == 'inc':
            def inc(x=x):
                registers[x] += 1
                registers['p'] += 1
            functions.append(inc)
        elif split[0] == 'dec':
            def dec(x=x):
                registers[x] -= 1
                registers['p'] += 1
            functions.append(dec)
        elif split[0] == 'jnz':
            def jnz(x=x, y=y):
                if x.isnumeric() and int(x) != 0:
                    registers['p'] += int(y)
                elif isinstance(x, str) and registers[x] != 0:
                    registers['p'] += int(y)
                else:
                    registers['p'] += 1
            functions.append(jnz)
            
    # Return the list of functions
    return functions

# Open input and read as strings
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# Init the registers. We also make one for the function pointer
registers = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'p':0
    }

# Parse the instructions
functions = parse(instructions)

# Run the code untill p is out of bounds
while(registers['p'] < len(functions)):
    # Run the p'th function
    functions[registers['p']]()

# Save the result from register a
roundOne = registers['a']

# Re init the registers
registers = {
    'a':0,
    'b':0,
    'c':1,
    'd':0,
    'p':0
    }

# Run the code untill p is out of bounds
while(registers['p'] < len(functions)):
    # Run the p'th function
    functions[registers['p']]()
    
# Save the result from round two
roundTwo = registers['a']

# Print the results
print(f'After the first round, the result in register a is {roundOne}')
print(f'After the second round, the result in register a is {roundTwo}')