# Function to get the next iteration
def getNextIteration(data):
    
    # The data
    a = data
    # And the data reversed with zeroes substituted for ones and vice verse
    b = ''.join(['0' if i == '1' else '1' for i in data[::-1]])
    
    # Joined with seperator
    return a + '0' + b
    
# Gets the biggest string that fits in the disk
def getBiggestString(data, diskSize):
    
    # While the data fits in the disk, get the next iteration
    while len(data) < diskSize:
        data = getNextIteration(data)
        
    # Cut off the data that don't fit
    return data[:diskSize]

# Gets the checksum for a string
def getCheckSum(data):
    
    # While the length of the data is even
    while len(data) % 2 == 0:
        
        # Get the new string
        data = ''.join(['1' if data[i] == data[i+1] else '0' for i in range(0,len(data),2)])
        
    return data

# The initial data
initial = '10111100110001111'

# Get the biggest string and checksum for the small disk
biggestString = getBiggestString(initial, 272)
checkSumShort = getCheckSum(biggestString)

# Get the biggest string and checksum for the large disk
biggestString = getBiggestString(initial, 35651584)
checkSumLong = getCheckSum(biggestString)

# Print the results
print(f'The checksum is {checkSumShort} for the small disk')
print(f'The checksum is {checkSumLong} for the large disk')