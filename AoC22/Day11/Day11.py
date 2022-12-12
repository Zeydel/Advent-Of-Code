# Class for the monkey
class Monkey:
    
    def __init__(self, items, operation, test, testval, throws):
        self.items = items
        self.operation = operation
        self.test = test
        self.testval = testval
        self.throws = throws
        self.inspections = 0

# Parse the descriptions into monkey objects
def parse(monkeys):
    
    # Init empty list
    objects = []
    
    # For every chunk of monkey description
    for m in range(0,len(monkeys),7):
        
        # Split and parse all the values
        items = [int(i.strip(',')) for i in monkeys[m+1].split()[2:]]
        op, val = monkeys[m+2].split()[4], monkeys[m+2].split()[5] 
        def operation(a, op=op, val=val):
            if op == '*':
                return a * (a if val == 'old' else int(val))
            else:
                return a + (a if val == 'old' else int(val))
        
        testval = int(monkeys[m+3].split()[3])
        def test(a, tv=testval):
            return True if a % tv == 0 else False
        onTrue = int(monkeys[m+4].split()[5])
        onFalse = int(monkeys[m+5].split()[5])
        
        # Create a monkey object and append to the list
        monkey = Monkey(items, operation, test, testval, (onTrue, onFalse))
        
        objects.append(monkey)
    
    # Return the monkeys
    return objects


# Function to do a round of monkey business. 
def doRound(monkeys, mod=None):
    
    # For every item of all the monkeys
    for m in range(len(monkeys)):
        for i in monkeys[m].items:
            
            # Increment inspections
            monkeys[m].inspections += 1
            
            # Either perform the with the given modulo or divided by three
            if mod == None:
                i = monkeys[m].operation(i) // 3
            else:
                i = monkeys[m].operation(i) % mod
            
            # Do the throw
            if monkeys[m].test(i):
                monkeys[monkeys[m].throws[0]].items.append(i)
            else:
                monkeys[monkeys[m].throws[1]].items.append(i)
        
        # Delete the items
        monkeys[m].items = []
            
    return monkeys
            

# Open input and read as strings
f = open('input.txt', 'r')
monkeysDescriptions = f.read().split('\n')

# Parse the monkeys
monkeys = parse(monkeysDescriptions)

# Do 20 rounds without a modulo
for i in range(20):
    monkeys = doRound(monkeys)


# Find the level of monkey business
monkeys = sorted(monkeys, key=lambda m: -m.inspections)
shortWorry = monkeys[0].inspections * monkeys[1].inspections

# Compute the product of all the monkeys test values (luckily they are prime)
mod = 1
for m in monkeys:
    mod *= m.testval

# Reset the monkeys
monkeys = parse(monkeysDescriptions)

# Do 10000 rounds of monkey business modulo the product
for i in range(10000):
    monkeys = doRound(monkeys, mod)
        
# Find the level of monkey business
monkeys = sorted(monkeys, key=lambda m: -m.inspections)
longWorry = monkeys[0].inspections * monkeys[1].inspections

print(f'After 20 rounds, the level of monkey business is {shortWorry}')
print(f'After 10000 rounds, the level of monkey business is {longWorry}')