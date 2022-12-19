from tqdm import tqdm

def parse(blueprintsText):
    
    blueprints = []
    
    for b in blueprintsText:
        
        b = b.split()
        
        oreCost = (int(b[6]),0,0,0)
        clayCost = (int(b[12]),0,0,0)
        obsidianCost = (int(b[18]), int(b[21]), 0,0)
        geodeCost = (int(b[27]), 0, int(b[30]), 0)
        
        blueprints.append((oreCost, clayCost, obsidianCost, geodeCost))
    
    return blueprints

def getMostGeodes(blueprint, timelimit, rocks, bots, seen, mostExpensive, time = 1):
        
    if (tuple(rocks), tuple(bots), time) in seen:
        return 0
    
    seen.add((tuple(rocks), tuple(bots), time))
    
    choices = [-1]  
    
    c = 1
    
    for i, b in enumerate(blueprint):
        
        if all([b[j] <= rocks[j] for j in range(len(b))]):
            c += 1
            if mostExpensive[i]*(timelimit-time) > rocks[i]+(bots[i]*(timelimit-time)):
                if b[i] < mostExpensive[i]:
                    choices.append(i)
                        
    for i, b in enumerate(bots):
        rocks[i] += b
    
    if c == 5:
        choices = choices[1:]
    
    if time == timelimit:
        return rocks[3]

    for i in choices:
        
        if i == -1:
            cGeodes = getMostGeodes(blueprint, timelimit, list(rocks), list(bots), seen, mostExpensive, time+1)
        else:
            cBots = list(bots)
            cBots[i] += 1
            cRocks = list(rocks)
            
            for c, j in enumerate(blueprint[i]):
                cRocks[c] -= j
            
            cGeodes = getMostGeodes(blueprint, timelimit, cRocks, cBots, seen, mostExpensive, time+1)
            
        
        if cGeodes > maxGeodes:
            maxGeodes = cGeodes
            
    return maxGeodes
        

# Open input and read as strings
f = open('input.txt', 'r')
blueprintsText = f.read().split('\n')

blueprints = parse(blueprintsText)

qualitySum = 0

#for i, b in enumerate(blueprints):
    
#    rocks = [0,0,0,0]
#    bots = [1,0,0,0]
#    seen = set()
    
#    mostGeodes = getMostGeodes(b, 23, rocks, bots, seen)
    
#    qualitySum += (i+1) * mostGeodes

product = 1

for i in range(3):
    
    rocks = [0,0,0,0]
    bots = [1,0,0,0]
    seen = set()
    
    mostExpensive = []
    
    for j in range(3):
        mostExpensive.append(max([blueprints[i][k][j] for k in range(4)]))
        
    mostExpensive.append(float('inf'))
    
    mostGeodes = getMostGeodes(blueprints[i], 32, rocks, bots, seen, mostExpensive)
    print(mostGeodes)
    
    product *= mostGeodes

print(qualitySum)
print(product)

#20979 not right
#10846 Too low