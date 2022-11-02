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

# Parses the list of strings into the a dict of reverse replacements,
# meaning that you get replacements that can be used to reduce the string
def getReverseReplacementDict(replacements):
    
    # Init empty dict
    reverseReplacements = dict()
    
    # Parse every lin
    for k in replacements:
        for v in replacements[k]:
            reverseReplacements[v] = k
            
    return reverseReplacements
        
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

# Okay, this one is kind of complicated. The problem can be solved by simply
# using the greedy approach, but the state space is massive. It would probably
# take years to search it throughly. However just by guessing a sequence of reduction
# there is a pretty high chance that you will find one that hits the target. I
# will try my best to explain the below code which tries to do something smarter.

# First, when we look at the dictionary of reverse replacements, we see that
# we have two different types of reductions:
# XX => X
# And
# X Rn X Ar | X Rn X Y X Ar | X Rn X Y X Y X Ar => X
# It should be noted that no strings reduce to Rn, Y or Ar
# The above can be thought about a bit simpler by replacing some string with signs:
# X ( X ) | X ( X , X ) | X ( X , X , X ) => X
# Now we can think about how long it takes to reduce this. Any string without
# Rn Ar or Y of length n reduces to length 1 in n-1 steps. So if we only have
# this case we can simply calculate the reduction length as 
# count(molecules) - 1
# Now, we can think of the other cases
# X Rn X Ar reduces to X in one step, but it reduces the length by 3 molecules
# X Rn X Y X Ar reduces to X in one step, but it reduces the length by 5 molecules
# X Rn X Y X Y X Ar reduces to X in one step, but it reduces the length by 7 molecules
# So, every one of these strings saves us some steps compared to the XX => X reductions
# Specifically, we get the Rn and Ar reduction for 'free', and every Y saves us
# two reductions (the character Y followed by any element). So, adding this to the
# formula from above, we get the formula:
# count(molecules) - count(Rn | Ar) - 2*count(Y) - 1
# This tells us exactly how many steps we need to reduce, which is just the reverse
# of the expansion and thus the same size
def findExpansionSize(molecule):
    moleculeCount = len(re.findall(r'[A-Z][a-z]|[A-Z]', molecule))
    RnArCount = len(re.findall(r'Rn|Ar', molecule))
    YCount = len(re.findall(r'Y', molecule))
    return moleculeCount - RnArCount - 2*YCount - 1
    
    
# Read input and parse
f = open('input.txt', 'r')
strings = f.read().split('\n')
molecule = strings[-1]
replacements = getReplacementDict(strings[0:-2])

print(f'{len(getSubstitutions(molecule, replacements))} different strings can be created from the starting string')
print(f'The minimum number of steps needed to expand e to {molecule} is {findExpansionSize(molecule)}')
