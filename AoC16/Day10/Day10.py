# Function to parse the instructions
def parse(instructions):
    
    # We want a dict of bots and their current chips
    bots = dict()
    # And their instructions for chage
    changes = dict()
    
    # For every instruction
    for i in instructions:
        # Split to parse easier
        split = i.split(' ')
            
        # If the line imples the instructionf for a bot change, parse it as such
        if split[0] == "bot":
            changes[int(split[1])] = ((split[5], int(split[6])), (split[10], int(split[11])))
        else:
            # Else parse it as starting instruction for a bot
            if int(split[5]) not in bots:
                bots[int(split[5])] = []
            bots[int(split[5])].append(int(split[1]))
            
    # Return bots and their change instructions
    return (bots, changes)

# Open input and read the string
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# Parse the instructions
bots, changes = parse(instructions)

# Make an empty set of for state exploration
nextBots = set()

# Init the output dict
outputs = dict()

# Var for the bot responsible for comparing chip 61 and chip 17
responsible = -1

# Find the bot(s) that have two chips in the beginning
for b in bots:
    if len(bots[b]) == 2:
        # Add those to exploration set
        nextBots.add(b)
        
# While we have something left to explore
while len(nextBots) > 0:
    # Get an element from the set
    cur = nextBots.pop()
    
    # If bot doesn't have two chips, continue
    if not len(bots[cur]) == 2:
        continue
    
    # Get the data from the dicts
    changeLow, changeHigh = changes[cur]
    low, high = min(bots[cur]), max(bots[cur])
    
    # Remove chips from bot
    bots[cur] = []
    
    # If we have found the responsible bot, save it
    if low == 17 and high == 61:
        responsible = cur
    
    # If we have to pass the low value to a bot, do so
    if changeLow[0] == "bot":
        if not changeLow[1] in bots:
            bots[changeLow[1]] = []
        bots[changeLow[1]].append(low)
        
        # Add the bot to the exploration space
        nextBots.add(changeLow[1])
    else:
        # Otherwise add it to the input
        outputs[changeLow[1]] = low
        
    # If we have to pass the high value to a bot, do so
    if changeHigh[0] == "bot":
        if not changeHigh[1] in bots:
            bots[changeHigh[1]] = []
        bots[changeHigh[1]].append(high)
        
        # Add the bot to the exploration space
        nextBots.add(changeHigh[1])
    else:
        # Otherwise add it to the input
        outputs[changeHigh[1]] = high

# Print the results
print(f'The bot responsbile for comparing chip 61 and 17 is bot number {responsible}')
print(f'The product of output 0, 1 and 2 is {outputs[0] * outputs[1] * outputs[2]}')