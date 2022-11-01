# Function to generate all increasing triples
def genIncreasingSequences():
    return set([chr(i)+chr(i+1)+chr(i+2) for i in range(97,121)])

# Function to count non-overlapping pairs
def countNonoverlappingPairs(password):
    pairs = 0
    i = 0
    while i < len(password)-1:
        
        # If we have found a match, count the pair and skip next
        # character
        if password[i] == password[i+1]:
            pairs += 1
            i += 1
        i += 1
            
    # Return the number of pairs
    return pairs

# Function to smartly increment the password, skipping all
# illegal characters
def smartIncrement(password):
    
    # If the final letter is not a z, just increment it
    if ord(password[-1]) < 122:
        return password[0:-1] + chr(ord(password[-1])+1)
    else:
        # If the final character is a z, remove it from the password and
        # increment
        password = smartIncrement(password[0:-1])
        
        # Replace illegal characters with the next one in the alphabet
        if password[-1] == 'i':
            password = password[0:-1] + 'j'
        if password[-1] == 'o':
            password = password[0:-1] + 'p'
        if password[-1] == 'l':
            password = password[0:-1] + 'm'
            
        # Return the password concatonated with a to account for the removed z
        return password + 'a'


# Function to check if a password lives up to the requirements
def isSafe(password):
    
    # If there are no íncreasing triples in the password, return false
    if not any([password[i:i+3] in inc for i in range(0,len(password)-3)]):
        return False
    
    # If there isn't at least two non overlapping pairs, return false
    if countNonoverlappingPairs(password) < 2:
        return False
    
    # Otherwise return True
    return True
    
# The original password
password = 'vzbxkghb'

# Generate the increasing sequences
inc = genIncreasingSequences()

# Whoæe we havent found a safe password
while not isSafe(password):
    
    # Increment the password
    password = smartIncrement(password)
    
# Save the found safe password
nextPassword = password

# Increment again
password = smartIncrement(password)

# Look for the next safe password
while not isSafe(password):
    password = smartIncrement(password)

# Save it
nextNextPassword = password
    
print(f'The next safe password is {nextPassword}')

print(f'And the one after that is {nextNextPassword}')