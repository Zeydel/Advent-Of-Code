# Parse the input into a dict of wires and their input
def parse(lines):
    
    wires = dict()
    
    for line in lines:
        
        if ':' in line:
            wire, signal = line.split(': ')
            wires[wire] = signal
        elif ' -> ' in line:
            signal, wire = line.split(' -> ')
            wires[wire] = tuple(signal.split())
            
    return wires

# Recursively get the input of a wire
def get_wire_value(wires, wire):
    
    if wires[wire] == '0' or wires[wire] == '1':
        return wires[wire]
    
    input1, condition, input2 = wires[wire]
    
    val1 = get_wire_value(wires, input1)
    val2 = get_wire_value(wires, input2)
    
    if condition == 'AND':
        if val1 == '1' and val2 == '1':
            wires[wire] = '1'
        else:
            wires[wire] = '0'
    elif condition == 'OR':
        if val1 == '1' or val2 == '1':
            wires[wire] = '1'
        else:
            wires[wire] = '0'
    elif condition == 'XOR':
        if val1 != val2:
            wires[wire] = '1'
        else:
            wires[wire] = '0'
            
    return wires[wire]

# Get all wire values
def get_wire_values(wires):

    wires_copy = dict(wires)    

    for wire in wires_copy:
        get_wire_value(wires_copy, wire)
        
    return wires_copy
        
# Get the decimal output on a set of wires
def get_output(wires, letter):
    
    z_number = 0
    
    wire_name = letter + '0' + str(z_number)
    
    binary_number = ''
    
    while wire_name in wires:
        
        binary_number = wires[wire_name] + binary_number
        
        z_number += 1
        z_number_str = str(z_number)
        
        if len(z_number_str) == 1:
            z_number_str = '0' + z_number_str
        
        wire_name = letter + z_number_str
        
    return int(binary_number, 2)
        
# Function to check wehter a specifc wire is part of a gate
def is_wire_gate(wires, wire, condition):
    
    for w in wires:
        
        if w[0] in ('x', 'y'):
            continue
        
        i1, cond, i2 = wires[w]
        
        if cond == condition and wire in (i1, i2):
            return True
        
    return False
        
# Get all wrong wires
def get_wrong_wires(wires, z_max):
    
    # Init set of wrong inputs
    wrong_inputs = set()
    
    # For every wire
    for wire in wires:
        
        # If it is an x or y wire, continue
        if len(wires[wire]) == 1:
            continue
        
        # Split into parts
        input1, condition, input2 = wires[wire]
        
        # XOR gates should only occur directly after x/y or directly before z
        if condition == 'XOR' and wire[0] != 'z' and input1[0] not in ('x', 'y'):
            wrong_inputs.add(wire)
            
        # AND should not be followed by XOR
        if condition == 'AND' and 'x00' not in (input1, input2) and is_wire_gate(wires, wire, 'XOR'):
            wrong_inputs.add(wire)
            
        # XOR Should not be followed by OR
        if condition == 'XOR' and 'x00' not in (input1, input2) and is_wire_gate(wires, wire, 'OR'):
            wrong_inputs.add(wire)
            
        # Z wires except for the last one should be preceded by XOR
        if condition != 'XOR' and wire[0] == 'z' and wire != z_max:
            wrong_inputs.add(wire)
                
    # Return the wrong inputs
    return wrong_inputs
        
# Open file and read as input
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse input
wires = parse(lines)

# Get wire values
wire_value = get_wire_values(wires)

# Get z output
z_output = get_output(wire_value, 'z')

# Get wrong wires
wrong = get_wrong_wires(wires, 'z45')

# Join their names together
wrong_string = ','.join(sorted(wrong))

# Print the outputs
print(f'{z_output} is the output on the z wires')
print(f'{wrong_string} are the swapped wires')
