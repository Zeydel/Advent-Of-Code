# Parse the text into a list of tuples of tuples
def parse(blueprintsText):
    
    # Init empty
    blueprints = []
    
    # For every line
    for b in blueprintsText:
        
        # Split to parse
        b = b.split()
        
        # And get the cost for every bot
        oreCost = (int(b[6]),0,0,0)
        clayCost = (int(b[12]),0,0,0)
        obsidianCost = (int(b[18]), int(b[21]), 0,0)
        geodeCost = (int(b[27]), 0, int(b[30]), 0)
        
        # Add the blueprint to the list
        blueprints.append((oreCost, clayCost, obsidianCost, geodeCost))
    
    return blueprints

# Function to find out if a a state is strictly better than another state
def isStrictlyBetter(previous, current):
    
    pRocks, pBots = previous
    cRocks, cBots = current

    # If we have at least as many bots and rocks, return true
    if all([pRocks[i] >= cRocks[i] for i in range(4)]):
       if all([pBots[i] >= cBots[i] for i in range(4)]):
           return True
       
    # Else return false
    return False
    
# Get the most possbile geodes using the blueprint
def getMostGeodes(blueprint, timelimit, rocks, bots, seen, mostExpensive, bestSoFar = 0, time = 1):
        
    # If we have not seen the current time yet, make a new set in the dict
    if time not in seen:
        seen[time] = set()
        
    # If any previousloy seen state of the same timestep is strictly better than the current, return 0
    if any([isStrictlyBetter(prev, (rocks, bots)) for prev in seen[time]]):
        return 0
    
    # Calculate the remaining time
    remaining = timelimit-time
    
    # If we cannot possibly obtain more geodes than the current best, return zero
    if (rocks[3]+bots[3]) + (bots[3]*remaining) + ((remaining*(remaining+1))//2) < bestSoFar:
        return 0

    # Add the current state the set set
    seen[time].add((tuple(rocks), tuple(bots)))
    
    # Add the "do nothing" choice
    choices = [-1]  
        
    # Choice counter
    choiceCount = 0
    
    # If we can afford to buy geode bots in all remaining rounds, just buy geode bots
    if all([rocks[i]+((remaining)*bots[i]) > b*(remaining) and rocks[i] >= b for i, b in enumerate(blueprint[3])]):
            choices = [3]
    else:            
        
        # Else find out what bots we can afford
        for i, b in enumerate(blueprint):
            if all([b[j] <= rocks[j] for j in range(len(b))]):
                choiceCount += 1
                        
                # If we already can afford the most expensive price of that rock, do not buy the bot
                if rocks[i] + (bots[i]*(remaining)) > mostExpensive[i]*(remaining):
                    continue
                        
                # If we have more bots than the most expensive price of the rocks, do not but that bot
                if bots[i] >= mostExpensive[i]:
                    continue
                        
                # Add the choice
                choices.insert(0,i)
                                
            # If we can afford everything, do not buy anything
            if choiceCount == 4 and len(choices) > 1:
                choices = choices[:-1]
            
            
    # Mine
    for i, b in enumerate(bots):
        rocks[i] += b
        
    # If we are at the timelimit, return the current number of geodes
    if time == timelimit:
        return rocks[3]

    # For every choice, recurse and save the best number of geodes so far
    for i in choices:
        
        if i == -1:
            bestSoFar = max(bestSoFar, getMostGeodes(blueprint, timelimit, list(rocks), list(bots), seen, mostExpensive, bestSoFar, time+1))
        else:
            cBots = list(bots)
            cBots[i] += 1
            cRocks = list(rocks)
            
            for c, j in enumerate(blueprint[i]):
                cRocks[c] -= j
            
            bestSoFar = max(bestSoFar, getMostGeodes(blueprint, timelimit, cRocks, cBots, seen, mostExpensive, bestSoFar, time+1))
            
    # Return the best so far
    return bestSoFar
        

# Open input and read as strings
f = open('input.txt', 'r')
blueprintsText = f.read().split('\n')

# Parse the blueprints
blueprints = parse(blueprintsText)

# Init var for sum
qualitySum = 0

# For every blueprint
for i, b in enumerate(blueprints):
        
    # Init starting state vars
    rocks = [0,0,0,0]
    bots = [1,0,0,0]
    seen = dict()
    mostExpensive = []

    for j in range(3):
        mostExpensive.append(max([b[k][j] for k in range(4)]))
        
    mostExpensive.append(float('inf'))
    
    # Find the most geodes
    mostGeodes = getMostGeodes(b, 24, rocks, bots, seen, mostExpensive)
    
    # Add the quality to the sum
    qualitySum += (i+1) * mostGeodes
        
# Init product
product = 1

# For the first three blueprints
for i in range(3):
    
    # Init starting state vars
    rocks = [0,0,0,0]
    bots = [1,0,0,0]
    seen = dict()
    
    mostExpensive = []
    
    for j in range(3):
        mostExpensive.append(max([blueprints[i][k][j] for k in range(4)]))
        
    mostExpensive.append(float('inf'))
        
    # Multiply the product on
    product *= getMostGeodes(blueprints[i], 32, rocks, bots, seen, mostExpensive)


print(f'The sum of qualities after 24 timesteps is {qualitySum}')
print(f'The product of the first three blueprints after 32 timesteps is {product}')
