# Parse the input into a graph
def parse(lines):
    
    graph = dict()
    
    for line in lines:
        
        pc1, pc2 = line.split('-')
        
        if pc1 not in graph:
            graph[pc1] = set()
            
        if pc2 not in graph:
            graph[pc2] = set()
            
        graph[pc1].add(pc2)
        graph[pc2].add(pc1)
        
    return graph

# Given a graph, a clique and a new vertex, returns true if
# adding the new vertex to the clique is still a clique
# otherwise returns false
def is_clique(graph, clique, new_vertex):
    
    for vertex in clique:
        
        if vertex not in graph[new_vertex]:
            return False
        
    return True
            
# Get all cliques in the graph
def get_cliques(graph):
    
    # Add a clique for each number
    cliques = set((number,) for number in graph)
    
    # Condition to break the loop
    new_clique_found = True
    
    max_size = 0
    
    # While we are still finding new cliques
    while new_clique_found:
        
        # Assume nothing new will be found
        new_clique_found = False
        
        # Add 1 to the max size
        max_size += 1
        
        # Set of new cliques
        new_cliques = set()
        
        # For every clique
        for clique in cliques:
            
            # If it is not the max size we are looking for
            if len(clique) != max_size:
                continue
            
            # Take a random vertex
            vertex = clique[0]
            
            # For each of its neighbors
            for new_vertex in graph[vertex]:
                
                # If it is alread in the clique, continue
                if new_vertex in clique:
                    continue
                
                # If adding the new vertex makes a new clique, add the new
                # clique to the set. Mark that we have found a new clique
                if is_clique(graph, clique, new_vertex):
                    new_cliques.add(tuple(sorted([*clique,new_vertex])))
                    new_clique_found = True
         
        # Add the new cliques to the set
        cliques |= new_cliques
        
    return cliques
            
# Get number of cliques where the historian could be
# that is, the number of cliques of size 3 where at least
# one vertex starts with t
def get_historian_cliques(cliques):
    
    historian_cliques = 0
    
    for clique in cliques:
        
        if len(clique) != 3:
            continue
        
        if any(v[0] == 't' for v in clique):
            historian_cliques += 1
            
    return historian_cliques

# Get the password. That is, get all vertices in the biggest clique
# ordered by name and seperated by commas
def get_password(cliques):
    
    max_size = 0
    max_clique = -1
    
    for clique in cliques:
        
        if len(clique) > max_size:
            max_clique = clique
            max_size = len(clique)
            
    return ','.join(sorted(max_clique))

# Open file and read as line
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Convert to graph
graph = parse(lines)

# Get all cliques
cliques = get_cliques(graph)

# Get number of historian cliques
historian_cliques = get_historian_cliques(cliques)

# Get the password
password = get_password(cliques)

# Print the results
print(f'{historian_cliques} is the number of sets of computers where the historian could be')
print(f'{password} is the password')