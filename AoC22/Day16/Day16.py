from itertools import combinations

# Def class for a node
class Node:
    
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.flow = 0
        self.children = []

# Parse the data into a dict
def parse(data):
    
    valves = dict()
    
    # For every line
    for d in data:
        
        # Split
        d = d.split()
        
        # Extract vars
        valve = d[1]
        flow = int(d[4].split('=')[1].strip(';'))
        tunnels = [t.strip(',') for t in d[9:]]
        
        # Add to dict
        valves[valve] = (flow, tunnels, False)
    
    # Return the dict
    return valves

# Get all pairwise distances for every node
def getDistances(valves):
    
    distances = dict()
    
    # For every valve
    for v in valves:
        
        # Do a BFS
        explored = set()
        explored.add(v)
        queue = []
        queue.append((v,0))
        
        while len(queue) > 0:
            cur = queue.pop(0)
            
            distances[(v, cur[0])] = cur[1]
            
            for n in valves[cur[0]][1]:
                if n not in explored:
                    queue.append((n, cur[1]+1))
                    explored.add(n)
                    
    # Return the dict
    return distances
                
# Build the Action Tree. A Tree over every action you can take
def buildActionTree(valves, distances, start, time = 1, timelimit = 30):
    
    # Create a node
    node = Node(start, time)
    
    # Calculate the flow and places we can go
    flow = 0
    targets = []
    for v in valves:
        if valves[v][2]:
            flow += valves[v][0]
        
        if not valves[v][2] and valves[v][0] > 0:
            targets.append(v)
    
    node.flow = flow
    
    # For every target
    for t in targets:
        
        # If we can get there in time
        if time + (distances[(start, t)]) < timelimit:
            
            # Mark the target as visited
            valvecopy = valves.copy()
            valvecopy[t] = (valves[t][0], valves[t][1], True)
            
            # Recurse with the new time
            node.children.append(buildActionTree(valvecopy, distances, t, time+distances[(start,t)] + 1, timelimit))
            
    # Return the node
    return node


# Function to find the best flow possible, given the action tree and timelimit
def findBestFlow(actionTree, timelimit):

    # Start with zero
    bestFlow = 0
    
    # All the possible actions
    toVisit = actionTree.children
    
    # If there are no actions, calculate the flow by just staying stilll
    if not toVisit:
        bestFlow = ((timelimit+1)-actionTree.time)*actionTree.flow
    else:
        
        # Otherwise, find the child with max flow
        for c in toVisit:
            bestFlow = max(bestFlow, (c.time-actionTree.time)*actionTree.flow + findBestFlow(c, timelimit))
        
    # Return the max
    return bestFlow

# Function to find all flows
def findAllFlows(actionTree, timelimit, flow = 0, current = []):
    
    # Start with an empty dict
    flows = dict()
    
    # If there are children, go through them
    if actionTree.children:
        for c in actionTree.children:
            
            # Add a dict entry for each child
            flows.update(findAllFlows(c, timelimit, flow + (c.time-actionTree.time)*actionTree.flow,  list(current) + [c.name]))
    
    # Also consider just standing still
    flows[(*current,)] = flow + ((timelimit+1)-actionTree.time)*actionTree.flow

    return flows

# Open input and read as strings
f = open('input.txt', 'r')
data = f.read().split('\n')

# Start position
start = 'AA'

# Parse the data and build an action tree with the time limit being 30
valves = parse(data)
distances = getDistances(valves)
actionTree = buildActionTree(valves, distances, start)

# Calculate the best flow
bestFlow = findBestFlow(actionTree, 30)

# Build a new tree of depth 30
actionTree = buildActionTree(valves, distances, start, timelimit = 26)

# Find all flows
allFlows = findAllFlows(actionTree, 26)

# Var for the best flow
bestFlowDuo = 0

# For every pair of flows, check if they are better than current best and that they are disjoint
for f1, f2 in combinations(allFlows, 2):
    if allFlows[f1] + allFlows[f2] > bestFlowDuo and set(f1).isdisjoint(set(f2)):
        bestFlowDuo = allFlows[f1] + allFlows[f2]
            
# Print the results
print(f'The best flow we can achieve is {bestFlow}')
print(f'The best flow we can achieve when working together is {bestFlowDuo}')
