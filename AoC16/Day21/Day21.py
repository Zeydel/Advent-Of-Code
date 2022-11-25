# Function to swap two positions in a string
def swapPos(password, X, Y):
   p = list(password)
   
   p[X], p[Y] = p[Y], p[X]
   
   return ''.join(p)

# Function to swap two letters in a string
def swapLetter(password, X, Y):
    p = list(password)
    iX = p.index(X)
    iY = p.index(Y)
    
    p[iX], p[iY] = p[iY], p[iX]

    return ''.join(p)

# Function to rotate a string left or right
def rotate(password, direction, X):
    if direction == 'left':
        X = -X
    
    return password[-X:] + password[:-X]

# Function to do rotation by letter
def rotateByLetter(password, X):
    p = list(password)
    iX = p.index(X)
    
    r = 1 + iX
    if iX >= 4:
        r += 1
        
    return password[-r % len(password):] + password[:-r % len(password)]

# Map needed to perform unscrambling of rotation by letter
UR = {
    0: -1,
    1: -1,
    2: -6,
    3: -2,
    4: -7,
    5: -3,
    6: 0,
    7: -4,
    }

# Perform unscramble of rotation by letter
def rotateByLetterUnscramble(password, X):
        
    iX = password.index(X)
    
    return password[-UR[iX]:] + password[:-UR[iX]] 

# Function to rotate a substring of the string
def reverse(password, X, Y):
    
    return password[:X] + ''.join(reversed(password[X:Y+1])) + password[Y+1:]

# Function to move a character to a given place in a string
def move(password, X, Y):
    p = list(password)
    l = p[X]
    del p[X]
    p.insert(Y, l)
    return ''.join(p)

# Function to scramble a password given a list of instructions
def scramble(password):

    # For every instruction
    for i in instructions:
        
        # Split to parse easier
        s = i.split()
        
        # Apply the given fucntion
        if s[0] == 'swap' and s[1] == 'position':
            password = swapPos(password, int(s[2]), int(s[5]))
        elif s[0] == 'swap':
            password = swapLetter(password, s[2], s[5])
        elif s[0] == 'rotate' and len(s) == 4:
            password = rotate(password, s[1], int(s[2]))
        elif s[0] == 'rotate':
            password = rotateByLetter(password, s[6])
        elif s[0] == 'reverse':
            password = reverse(password, int(s[2]), int(s[4]))
        else:
            password = move(password, int(s[2]), int(s[5]))
            
    # Return the scrambled string
    return password
        
# Function to unscramble a password
def unscramble(scrambled):
    
    # For every instruction read backwards
    for i in instructions[::-1]:
        
        # Split to parse easier
        s = i.split()
        
        # Apply the given function
        if s[0] == 'swap' and s[1] == 'position':
            scrambled = swapPos(scrambled, int(s[5]), int(s[2]))
        elif s[0] == 'swap':
            scrambled = swapLetter(scrambled, s[5], s[2])
        elif s[0] == 'rotate' and len(s) == 4:
            scrambled = rotate(scrambled, 'right' if s[1] == 'left' else 'left', int(s[2]))
        elif s[0] == 'rotate':
            scrambled = rotateByLetterUnscramble(scrambled, s[6])
        elif s[0] == 'reverse':
            scrambled = reverse(scrambled, int(s[2]), int(s[4]))
        else:
            scrambled = move(scrambled, int(s[5]), int(s[2]))
            
    # Return the unscrambled string
    return scrambled

    

# Read and parse the input
f = open('input.txt', 'r')
instructions = f.read().split('\n')

# Password and scrambled password
password = 'abcdefgh'
scrambled = 'fbgdceah'

# Print the result
print(f'The result of scrambling the password is {scramble(password)}')
print(f'The result of unscrambling the scrambled password is {unscramble(scrambled)}')