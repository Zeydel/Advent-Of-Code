# Parse instructions into a dicct
def parse(instructions):
    
    # Init empty
    monkeys = dict()
    
    # For every instruction
    for i in instructions:
        
        # Split
        i = i.split(": ")
        
        # If it is just a value, save it
        if i[1].isnumeric():
            monkeys[i[0]] = int(i[1])
            
        # Otherwise save the split calculation
        else:
            monkeys[i[0]] = i[1].split()
            
    return monkeys
        
# Function to get the value of a monkey
def getMonkeyValue(monkeys, monkey):
    
    # If the instruction is just an int or None, return it
    if isinstance(monkeys[monkey], int) or monkeys[monkey] == None:
        return monkeys[monkey]
    
    # Otherwise recurse left and right
    m1 = getMonkeyValue(monkeys, monkeys[monkey][0])
    m2 = getMonkeyValue(monkeys, monkeys[monkey][2])
    
    # If one of the subtrees is None, return None
    if m1 == None or m2 == None:
        return None

    # Otherwise perform a calculation
    if monkeys[monkey][1] == '+':
        return m1 + m2
    elif monkeys[monkey][1] == '*':
        return m1 * m2
    elif monkeys[monkey][1] == '/':
        return m1 // m2
    elif monkeys[monkey][1] == '-':
        return m1 - m2

# Function to get missing value
def getMissingValue(monkeys, monkey, targetValue = None):
    
    # If the monkeys value is none, return the target value
    if monkeys[monkey] == None:
        return targetValue
    
    # If the monkey just have value, return it
    if isinstance(monkeys[monkey], int):
        return monkeys[monkey]
    
    # Get both monkeys value
    m1 = getMonkeyValue(monkeys, monkeys[monkey][0])
    m2 = getMonkeyValue(monkeys, monkeys[monkey][2])
    
    # Find the value we know, and the monkey to recurse into
    if m1 == None:
        fixed = m2
        newMonkey = monkeys[monkey][0]
    else:
        fixed = m1
        newMonkey = monkeys[monkey][2]
        
    # Based on the sign, calculate the new number to reach the target value and recurse
    if monkeys[monkey][1] == '+':
        return getMissingValue(monkeys, newMonkey, targetValue - fixed)
    elif monkeys[monkey][1] == '*':
        return getMissingValue(monkeys, newMonkey, targetValue // fixed)
    elif monkeys[monkey][1] == '/':
        if isinstance(m1, int):
            return getMissingValue(monkeys, newMonkey, fixed // targetValue)
        else:
            return getMissingValue(monkeys, newMonkey, fixed * targetValue)
    elif monkeys[monkey][1] == '-':
        if isinstance(m1, int):
            return getMissingValue(monkeys, newMonkey, fixed - targetValue)
        else:
            return getMissingValue(monkeys, newMonkey, fixed + targetValue)
    elif monkeys[monkey][1] == '=':
        return getMissingValue(monkeys, newMonkey, fixed)


# Open input and read as strings
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# Parse the monkeys and get the monkey value
monkeys = parse(instructions)
monkeyValue = getMonkeyValue(monkeys, 'root')

# Set some vars for part 2
monkeys['root'][1] = '='
monkeys['humn'] = None

# Find the missing value
missingValue = getMissingValue(monkeys, 'root')

# Print the results
print(f'The monkey value is {monkeyValue}')
print(f'The value to yell is {missingValue}')