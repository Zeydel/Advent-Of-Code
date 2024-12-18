# Prase the input into initial register values and program code
def parse(lines):
    
    registers = dict()
    
    registers[4] = int(lines[0].split(' ')[-1])
    registers[5] = int(lines[1].split(' ')[-1])
    registers[6] = int(lines[2].split(' ')[-1])
    
    # Register for the pointer
    registers[-1] = 0
    
    codes = [int(num) for num in lines[-1].split(' ')[1].split(',')]
    
    return registers, codes

# Get the value of a combo operand
def get_combo_operand_value(registers, operand):
    if operand > 3:
        return registers[operand]
    return operand

# Fast version of running the pgraom
def run_program_fast(registers, target = []):

    A = registers[4]
    B = registers[5]
    C = registers[6]    

    output = []

    while A != 0:
        
        B = get_print_val(A)
        
        A = A // 8
        
        output.append(B)
        
        if target != [] and target[:len(output)] != output:
            return output 
        
    return output

# Given a value of register a, returns value that will be printed
def get_print_val(A):
    return ((((A % 8) ^ 1) ^ (A // (2 ** ((A % 8) ^ 1)))) ^ 4) % 8
    
# Find the lowest a value that will produce a code
def find_lowest_a(code, start = 0):
    
    # If there are no more value to search for stop
    if code == []:
        return start
    
    
    # The given program performs a //8 operation
    # after each iteration. We do the opposite here
    start *= 8
    
    # Init val for lowest a
    lowest_a = float('inf')
    
    # We are looking for the last value
    target = code[-1]
    
    # For the next 8 possible values of a
    for a in range(start, start+8):
        
        # Get the printed value
        print_val = get_print_val(a) 
       
        # If we have found the correct value, search for the lowest
        # value to get the next last value
        if print_val == target:
            lowest_a = min(lowest_a, find_lowest_a(code[:-1], a))
    
    # Return the lowest value
    return lowest_a
        
        
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
registers, code = parse(lines)

# Run the program
output = run_program_fast(registers)

# Compute the output string
output_string = ','.join([str(num) for num in output])

# Get the lowest a value to craete the code
lowest_a_value = find_lowest_a(code)

# Output the results
print(f'{output_string} is the result of running the code')
print(f'{lowest_a_value} is the lowest initial register that produces the progam again')
