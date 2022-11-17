# Hashlib to hash stuff
import hashlib

# The door ID
doorId = 'ffykfhsq'

# Vars for the passwords and a counter
passwordOne = ''
passwordTwo = '!!!!!!!!'
counter = 0

# While we havent solved both passwords
while len(passwordOne) < 8 or '!' in passwordTwo:
    
    # Get the hex of the hash of the door plus the current value of the counter
    hashHex = hashlib.md5((doorId + str(counter)).encode()).hexdigest()
    # If it starts with 5 zeros
    if hashHex[0:5] == '00000':
        
        # If we havent yet filled out the first password, add the sixth character in the hash to it
        if len(passwordOne) < 8:
            passwordOne += hashHex[5]
        
        # If sixth position is a digit AND its within the bounds of the password AND we havent filled in that place yet
        if hashHex[5].isdigit() and int(hashHex[5]) < len(passwordTwo) and passwordTwo[int(hashHex[5])] == '!':
            # Add the seventh value to the sixth place in the password
            passwordTwo = passwordTwo[:int(hashHex[5])] + hashHex[6] + passwordTwo[int(hashHex[5])+1:]
        
    # Increment the counter
    counter += 1
    
# Print the results
print(f'The first password is {passwordOne}')
print(f'The second password is {passwordTwo}')