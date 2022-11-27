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
                registers[y] = int(x) if x.lstrip("-").isnumeric() else registers[x]
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
                
                jmp = int(y) if y.lstrip("-").isnumeric() else registers[y]
                
                if x.isnumeric() and int(x) != 0:
                    registers['p'] += jmp
                elif not x.isnumeric() and isinstance(x, str) and registers[x] != 0:
                    registers['p'] += jmp
                else:
                    registers['p'] += 1
            functions.append(jnz)
        elif split[0] == 'tgl':
            def tgl(x=x):
                if registers[x] + registers['p'] >= len(functions):
                    registers['p'] += 1
                    return
                
                defaults = functions[registers['p'] + registers[x]].__defaults__
                
                if functions[registers['p'] + registers[x]].__code__.co_argcount == 1:
                    if functions[registers['p'] + registers[x]].__name__ == 'inc':
                        def dec(x=defaults[0]):
                            registers[x] -= 1
                            registers['p'] +=1
                        functions[registers['p'] + registers[x]] = dec
                    else:
                        def inc(x=defaults[0]):
                            registers[x] += 1
                            registers['p'] += 1
                        functions[registers['p'] + registers[x]] = inc
                else:
                    if functions[registers['p'] + registers[x]].__name__ == 'jnz':
                        def cpy(x=defaults[0], y=defaults[1]):
                            registers[y] = int(x) if x.isnumeric() else registers[x]
                            registers['p'] += 1
                        functions[registers['p'] + registers[x]] = cpy
                    else:
                        def jnz(x=defaults[0], y=defaults[1]):
                            
                            jmp = int(y) if y.lstrip("-").isnumeric() else registers[y]
                            
                            if x.isnumeric() and int(x) != 0:
                                registers['p'] += jmp
                            elif isinstance(x, str) and registers[x] != 0:
                                registers['p'] += jmp
                            else:
                                registers['p'] += 1
                        functions[registers['p'] + registers[x]] = jnz
                registers['p'] += 1
            functions.append(tgl)
        elif split[0] == 'out':
            def tgl(x=x):
                registers['o'].append(int(x) if x.lstrip("-").isnumeric() else registers[x])
                registers['p'] += 1
            functions.append(tgl)

                    
            
    # Return the list of functions
    return functions

# Return true only if it is a sequence of 0,1,0,1 repeating
def isValid(sequence):
    
    if any([s == 1 for s in sequence[::2]]):
        return False
    
    if any([s == 0 for s in sequence[1::2]]):
        return False
    
    return True

# Open input and read as strings
f = open('input.txt', 'r')
instructions = f.read().split('\n')


# Parse the instructions
functions = parse(instructions)

# We havent found the result yet
found = False

# Start by guessing 1
guess = 1
while not found:
    
    # Init the registers. We also make one for the function pointer
    registers = {
        'a':guess,
        'b':0,
        'c':0,
        'd':0,
        'p':0,
        'o':[]
        }
    
    # Run the code untill p is out of bounds
    while(registers['p'] < len(functions)):
        # Run the p'th function
        functions[registers['p']]()
        
        # If the output sequence is not valid, try again with a higher number
        if not isValid(registers['o']):
            guess += 1
            break
        
        # If the output sequence is more than 20 characters and valid, assume it goes on forever
        if len(registers['o']) > 20 and isValid(registers['o']):
            found = True
            break

# Print the result
print(f'The lowest number that produces the correct result is {guess}')
