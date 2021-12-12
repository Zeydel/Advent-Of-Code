# Function to find number of paths using the definition from part 1
def find_all_paths(adjecencies, cur_node, visited, cur_path, paths = 0):
        
    # If we are at the end, we have found a path. Increment counter
    if cur_node == 'end':
        return paths + 1
    
    # If current cave is lowercase, we add it to visited list
    if cur_node.islower():
        visited.add(cur_node)
        
    # Update current path with node
    cur_path = cur_path + [cur_node]

    # Find the list of next possible nodes. Exlcude already visited nodes
    next_possible = list(filter(lambda a: a not in visited, adjecencies[cur_node]))
    
    # Go through next possibilites and find all paths
    for n in next_possible:
        paths = find_all_paths(adjecencies, n, visited, cur_path, paths)
    
    # Remove current node from visited list
    if cur_node.islower():
        visited.remove(cur_node)

    # Return list of paths
    return paths
        
# Function to find number of paths using the definition from part 2
def find_all_paths_v2(adjecencies, cur_node, visited, cur_path, paths = 0):
 
    # If we are at the end, we have found a path. Increment counter
    if cur_node == 'end':
        return paths + 1
 
    # If current cave is lowercase, we add it to visited list
    if cur_node.islower():
        visited.add(cur_node)
        
    # Update current path with node
    cur_path = cur_path + [cur_node]
    
    # Find out if we have visited any lowercase cave twice
    visited_twice = False
    if any([cur_path.count(n) == 2 and n.islower() for n in cur_path]):
        visited_twice = True
    
    # List of next possible caves
    next_possible = []
    
    # If we have not visited a cave twice
    if not visited_twice:
        
        # Next possible cave is just adjecency list except for start cave
        next_possible = adjecencies[cur_node]
        if 'start' in next_possible:
            next_possible.remove('start')    
    else: # Else list is adjecency list except for visited nodes
        next_possible = list(filter(lambda a: a not in visited, adjecencies[cur_node]))
    
    # Go through list of possibilites and find all paths
    for n in next_possible:
        paths = find_all_paths_v2(adjecencies, n, visited, cur_path, paths)

    # Remove current node from visited list and current path
    cur_path.pop()
    if cur_node in visited and cur_node not in cur_path:
        visited.remove(cur_node)

    # Return the number of paths
    return paths    

# Open file and read as list of strings
f = open('input.txt', 'r')
lines = f.read().split('\n')

# Init adjecency list as empty dict
adjecencies = dict()

# Go through all lines
for l in lines:
    
    # Split line on -
    l_split = l.split('-')
    
    # Add keys if they do not exists
    if l_split[0] not in adjecencies:
        adjecencies[l_split[0]] = []
    
    if l_split[1] not in adjecencies:
        adjecencies[l_split[1]] = []
        
    # Add to adjecency lists
    adjecencies[l_split[0]].append(l_split[1])
    adjecencies[l_split[1]].append(l_split[0])
    
# Find number of paths for the first part
paths = find_all_paths(adjecencies, 'start', set(), [])
print('There are ' + str(paths) + ' ways through the caves')

# Find number of paths for the second part
paths_v2 = find_all_paths_v2(adjecencies, 'start', set(), [])
print('There are ' + str(paths_v2) + ' ways through the caves using the second method')