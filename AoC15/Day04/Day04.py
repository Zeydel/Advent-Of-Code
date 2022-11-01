# Import lib needed for hashing
import hashlib

# The secret key
secretKey = 'ckczppom'

# Init some starting variables
fiveZeroes = -1
sixZeroes = -1
number = 1

# Repeat until we find a solutions to the second part
while sixZeroes == -1:
    
    # Encode the secret key concatonated with the number and find the hex value
    md5 = hashlib.md5((secretKey + str(number)).encode()).hexdigest()
    
    # If we havent found a value for five zeroes, and the current hash
    # matches, save it
    if fiveZeroes == -1 and md5[0:5] == '00000':
        fiveZeroes = number
        
    # If we find a solutions for six zeroes, save it. This will break the loop
    if md5[0:6] == '000000':
        sixZeroes = number
        
    # Increment the number
    number += 1

print(f'{fiveZeroes} is the first number that produces a hash value with 5 leading zeroes')
print(f'{sixZeroes} is the first number that produces a hash value with 6 leading zeroes')