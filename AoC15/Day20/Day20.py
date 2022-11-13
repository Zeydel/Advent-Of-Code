# Need thjs to find square roots
import math

# Function to get the number of presents delivered to a house
def getNumberOfPresents(houseNumber):
    
    # Init zero presents
    presents = 0
    
    # For every number up to the root of the house number
    for i in range(1, int(math.sqrt(houseNumber))+1):    
        
        # If the house number is divisible by i
        if houseNumber % i == 0:
            
            # Add the divisor and its inverse, as long as it ins't the square root
            presents += i
            if not i*i == houseNumber:
                presents += (houseNumber/i)
                
    # Return the number of presents
    return presents*10
            
        
# Function to get the new number of presents delivered to a house
def getNewNumberOfPresent(houseNumber):
    
    # Init zero presents
    presents = 0
    
    # For every number up to the root of the house number
    for i in range(1, int(math.sqrt(houseNumber))+1):
        
        # If the house number is divisible by i
        if houseNumber % i == 0:
            
            # And elf i hasn't delievered 50 presents
            if houseNumber <= i*50:
                
                # Add a present to the house
                presents += i
                
            # Add the inverse, if it isn't the square root
            if not i*i == houseNumber and houseNumber <= (houseNumber/i)*50:
                presents += (houseNumber/i)
                
    # Return the number of presents
    return presents * 11
        
           
# The input
input = 36000000

# Some starting variables
houseNumber = 1
firstHouse = -1
newFirstHouse = -1

# While we haven't found both solutions
while firstHouse == -1 or newFirstHouse == -1:
    
    # Check if the current houseNumber solves the first problem
    if firstHouse == -1 and getNumberOfPresents(houseNumber) >= input:
        firstHouse = houseNumber
    
    # Check if the current houseNumber solves the second problem
    if newFirstHouse == -1 and getNewNumberOfPresent(houseNumber) >= input:
        newFirstHouse = houseNumber
    
    # Increment the house number
    houseNumber += 1
    
# Print the results
print(f'{firstHouse} is the first house to get {input} presents')
print(f'{newFirstHouse} is the new first house to get {input} presents')