# Function to parse a list of strings into a dict of instructions
def parse(strings):
    
    # Start with an empty dictionary
    instructions = {}
    
    # For every string
    for s in strings:
        
        # Make a dict so we can find insrtuctions for a specific
        # wire in constant time
        split = s.split(' -> ')
        instructions[split[1]] = split[0]
        
    # Return the instructions
    return instructions

# Function for finding the signal in a specific wire
def getSignal(var):
    
    # If we have already calculated the value in a wire, just return it
    if var in signals:
        return signals[var]

    # If the value is numeric, just return it (as an int)
    if var.isnumeric():
        return int(var)
    
    # Split the instructions for easier parsing
    i = instructions[var].split(' ')

    # If the length is 1, just get the value of the instruction
    if len(i) == 1:
        signals[var] = getSignal(i[0])
    # If the length is two, it must be a NOT. Do a binary negation of
    # the signal
    elif len(i) == 2:
        signals[var] = ~getSignal(i[1])
    # Else, it must be of length 3. Get signals for both input wires
    # and perform the needed binary operation
    elif i[1] == 'AND':
        signals[var] = getSignal(i[0]) & getSignal(i[2])
    elif i[1] == 'OR':
        signals[var] = getSignal(i[0]) | getSignal(i[2])
    elif i[1] == 'LSHIFT':
        signals[var] = getSignal(i[0]) << getSignal(i[2])
    elif i[1] == 'RSHIFT':
        signals[var] = getSignal(i[0]) >> getSignal(i[2])
        
    # Return the wire we asked for
    return signals[var]

# Read as strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Parse the strings to a dict
instructions = parse(strings)

# Create an empty dict to memoize wire signals
signals = {}

# Get the value in a after the first run
first_run = getSignal('a')

# Override wire b with the signal from a
instructions['b'] = str(signals['a'])

# Reset the signals
signals = {}

# Get the value in a after the second run
second_run = getSignal('a')

# Print the results
print(f'The signal in a after the first run is {first_run}')
print(f'The signal in a after the second run is {second_run}')