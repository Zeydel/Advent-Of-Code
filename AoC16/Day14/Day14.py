# Hash functions and regex
from hashlib import md5
import re

# Hashes the string 2017 times
def hash2016(string):
    
    for i in range(0, 2017):
        string = md5(string.encode()).hexdigest()
    
    return string

# Map of found quintuples
quintMap = dict()

# Function to check whether the next thousand hashes contain a quinuple of a given letter
def isValid(index, triple):    
    
    # For the next thousand indices
    for i in range(index+1, index+1000):
        # If we havent checked it yet
        if i not in quintMap:
            # Compute the hash
            hashed = md5((salt + str(i)).encode()).hexdigest()
            # Find all quintuples and add to map
            quints = re.findall(r'([a-z0-9])\1\1\1\1', hashed)
            quintMap[i] = quints
        
        # If the triple is in the quintmap, return true
        if triple in quintMap[i]:
            return True
        
    # Otherwise, it is not valid
    return False
            
# The same as above, but using the 2017 times hash
quintMap2016 = dict()
def isValid2016(index, triple):
    
    for i in range(index+1, index+1000):
        if i not in quintMap2016:
            hashed = hash2016(salt + str(i))
            quints = re.findall(r'([a-z0-9])\1\1\1\1', hashed)
            quintMap2016[i] = quints
        
        if triple in quintMap2016[i]:
            return True
        
    return False

# The salt
salt = 'cuanljph'

# The keys
keys = ''
keys2016 = ''

# Init the index
index = 0

# And vars for the result
endIndex = -1
endIndex2016 = -1

# While the key is below 64 letters
while len(keys) < 64:
    # Compute the hash of the salt plus the index
    hashed = md5((salt + str(index)).encode()).hexdigest()
    
    # Find triples
    repeat = re.search(r'([a-z0-9])\1\1|$', hashed).group()
    
    # If there is a repeat, and it is valid, add it to the string
    if repeat and isValid(index, repeat[0]):
        keys += str(repeat[0])
        
        # If the key is 64 chars long, and we havent found a result yet
        # save the current index
        if len(keys) == 64 and endIndex == -1:
            endIndex = index

    index += 1

# Reset the index, and do the same thing as above, but with 2017 hashes
index = 0

while len(keys2016) < 64:
    hashed = hash2016(salt + str(index))
    repeat = re.search(r'([a-z0-9])\1\1|$', hashed).group()

    if repeat and isValid2016(index, repeat[0]):
        keys2016 += str(repeat[0])
        
        if len(keys2016) == 64 and endIndex2016 == -1:
            endIndex2016 = index
            
    index += 1
    
# Print the results
print(f'Index {endIndex} produces the 64th key')
print(f'Index {endIndex2016} produces the 64th key if you hash 2017 times')
