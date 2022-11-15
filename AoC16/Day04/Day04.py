# Need regex to find integers
import re

# Function to get expected checksum given a room name
def getExpectedChecksum(room):
    # We dont care about dashes
    room = room.replace('-', '')
    # Init a counting dict
    letters = dict()
    
    # Count occurences of letters
    for l in room:
        if not l in letters:
            letters[l] = 0
        letters[l] += 1
        
    # Sort by occurences, then alphabetically
    sortedLetters = sorted(letters, key=lambda l: (-letters[l],l))

    # Return a string of the first 5
    return ''.join(sortedLetters[0:5])

# Function to decode a room name
def decodeName(room, roomNumber):
    decoded = ''
    
    # For every letter
    for l in room:
        # Replace dash by space
        if l == '-':
            decoded += ' '
        else:
            # Get the letter down to the range 0-25
            d = ord(l)-97
            # Add the room number
            d += roomNumber
            # Get the letter down to the range 0-25 by taking the modulo
            d %= 26
            # Add 97 again to get up to ascii space
            d += 97
            # Add the corresponding char to the string
            decoded += chr(d)
    
    # Return the decoded string
    return decoded

# Open input and read as 2d array of integers
f = open('input.txt', 'r')
rooms = f.read().split('\n')

# Vars to store the result
roomNumberSum = 0
northPoleObjectStorage = -1

# For every room
for r in rooms:
    # Parse the string
    checksum = r.split('[')[1][:-1]
    split = re.search(r'\d+', r)
    roomNumber = int(split.group())
    name = r[0:split.start()]
    
    # If we get the expected checksum, the room is real
    if getExpectedChecksum(name) == checksum:
        # Add the number to the sum
        roomNumberSum += roomNumber
        
        # Decode the name
        decodedName = decodeName(name, roomNumber)
        # If the name contains the three keywords, we assume that is the right one
        if all(i in decodedName for i in ['north', 'pole', 'object']):
            northPoleObjectStorage = roomNumber
        
# Print the results
print(f'The sum of the real room numbers is {roomNumberSum}')
print(f'The north pole objects are stored in room {northPoleObjectStorage}')
    