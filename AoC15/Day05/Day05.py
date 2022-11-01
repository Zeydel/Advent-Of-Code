# Sets needed for checking
vowels = {'a','e', 'i','o','u'}
badStrings = {'ab', 'cd', 'pq', 'xy'}

# Checks if a string is nice according to the old rules
def isStringNice(string):
    # Returns false if list contains less than 3 vowels
    if sum([1 if c in vowels else 0 for c in string]) < 3:
        return False
    # Returns false if string does not contain any duplicate letters
    if not any([string[i] == string[i+1] for i in range(len(string)-1)]):
        return False
    # Returns false if string contains any of the bad strings
    if any([string[i:i+2] in badStrings for i in range(len(string)-1)]):
        return False
    
    # If we haven't broken any rules, string must be nice
    return True
    
# Checks if a string is nice according to the new rules
def newIsStringNice(string):
    
    # Returns false if string does not contain a non-overlapping duplicate string of length 2
    if not any([string[i:i+2] in string[i+2:] for i in range(len(string)-2)]):
        return False
    # Returns false if string does not contain two similar characters seperated by another character
    if not any([string[i] == string[i+2] for i in range(len(string)-2)]):
        return False
    
    # If we haven't broken any rules, string must be nice
    return True

# Read input as list of strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Init counters
niceStrings = 0
newNiceStrings = 0

# For each string
for s in strings:
    
    # Perform checks by both new and old system. 
    if isStringNice(s):
        niceStrings += 1
    if newIsStringNice(s):
        newNiceStrings += 1
        
print(f'{niceStrings} strings are nice according to the old system')
print(f'{newNiceStrings} strings are nice according to the new system')