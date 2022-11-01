import re

# Parses the list of replacments into a dictionary
def getReplacementDict(strings):
    
    # Init empty dict
    replacements = dict()
    
    # For every line
    for s in strings:
        
        # Split the string
        split = s.split()
        
        # If we haven't seen the key already add it with an empty list
        if split[0] not in replacements:
            replacements[split[0]] = []
            
        # Add the value to the list
        replacements[split[0]].append(split[2])
        
    return replacements

def getReverseReplacementDict(replacements):
    
    reverseReplacements = dict()
    
    for k in replacements:
        for v in replacements[k]:
            reverseReplacements[v] = [k]
            
    return reverseReplacements
        
# Returns the set of molecules you can get from a starting molecule and a 
# list of substitutions you can perform
def getSubstitutions(molecule, replacements):
    
    # Init empty set
    newMolecules = set()
    
    # For every substring that can be replaced
    for k in replacements:
        # For every index of the string
        for s in [m.start() for m in re.finditer(k, molecule)]:
            # For every possible replacement
            for r in replacements[k]:
                # Add the resulting string to the set
                newMolecules.add(molecule[:s] + r + molecule[s+len(k):])
    return newMolecules

def getNextRound(molecules, replacements):
    
    nextRound = set()
    
    for m in molecules:
        nextRound |= getSubstitutions(m, replacements)
        
    print(len(nextRound))
    return nextRound
    
def expandGreedy(molecule, target, replacements, depth = 0, maxdepth = float('inf')):
    
    if molecule in seen:
        return maxdepth
    
    seen.add(molecule)
    
    if molecule == target:
        return depth
    
    if len(molecule) >= len(target):
        return maxdepth
    
    for s in getSubstitutions(molecule, replacements):
        maxdepth = min(expandGreedy(s, target, replacements, depth+1, maxdepth), maxdepth)
    
    return maxdepth
    
    
# Read input and parse
f = open('input.txt', 'r')
strings = f.read().split('\n')
molecule = strings[-1]
replacements = getReplacementDict(strings[0:-2])
reverseReplacements = getReverseReplacementDict(replacements)
seen = set()
current = {'e'}
rounds = 0


print(expandGreedy('e', molecule, replacements))
print(len(getSubstitutions(molecule, replacements)))
