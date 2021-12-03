# Function to get decimal value of a binary string
def getDecimalValue(binary):
    if binary == '':
        return 0
    
    if binary[0] == '1':
        return (2 ** (len(binary)-1)) + getDecimalValue(binary[1:])
    else:
        return getDecimalValue(binary[1:])

# Function to byte consisting of most common bits from list of bytes
def getMostCommonByte(byte_list):
    
    # Init empty string
    most_common_byte = ''
    
    # For each bit
    for i in range(len(byte_list[0])):
        
        # Init pointers
        zero_count = one_count = 0
        
        # Count number of ones and zeros
        for b in byte_list:
            if b[i] == '0':
                zero_count += 1
            else:
                one_count += 1
                
        # Append most common bit
        if zero_count > one_count:
            most_common_byte += '0'
        else:
            most_common_byte += '1'
    
    # Return constructed string
    return most_common_byte

# Get the inverse of a byte
def getInverseByte(byte):
    new_byte = ''
    
    # For each bit, append the inverse
    for c in byte:
        if c == '0':
            new_byte += '1'
        else:
            new_byte += '0'
            
    return new_byte

# Function to get the oxygen generator rating
def getOxygenGeneratorRating(byte_list, pos = 0):
    
    # If list only has one element, return it
    if(len(byte_list) == 1):
        return byte_list[0]
    
    # Init counters
    zero_count = one_count = 0
    
    # For each byte, count the ones and zeros at the curent position
    for b in byte_list:
        if b[pos] == '0':
            zero_count += 1
        else:
            one_count += 1
    
    # Recursively call with filtered list and next position
    if (zero_count > one_count):
        return getOxygenGeneratorRating(list(filter(lambda byte: byte[pos] == '0', byte_list)), pos + 1)
    else:
        return getOxygenGeneratorRating(list(filter(lambda byte: byte[pos] == '1', byte_list)), pos + 1)

# Function to get CO2 scrubber rating
def getCO2ScrubberRating(byte_list, pos = 0):
    
    # If list only has one element, return it
    if(len(byte_list) == 1):
        return byte_list[0]
    
    # Init counters
    zero_count = one_count = 0
    
    # For each byte, count the ones and zeros at the curent position
    for b in byte_list:
        if b[pos] == '0':
            zero_count += 1
        else:
            one_count += 1
    # Recursively call with filtered list and next position
    if (one_count < zero_count):
        return getCO2ScrubberRating(list(filter(lambda byte: byte[pos] == '1', byte_list)), pos + 1)
    else:
        return getCO2ScrubberRating(list(filter(lambda byte: byte[pos] == '0', byte_list)), pos + 1)

# Open file and read input
f = open('input.txt')
byte_list = f.read().split()

# Get values needed for first part
most_common_byte = getMostCommonByte(byte_list)
gamma_rate = getDecimalValue(most_common_byte)
epsilon_rate = getDecimalValue(getInverseByte(most_common_byte))

# Get values needed for second part
oxygen_generator_rating = getDecimalValue(getOxygenGeneratorRating(byte_list))
CO2_scrubber_rating = getDecimalValue(getCO2ScrubberRating(byte_list))

# Print the results
print('The gamma rate multiplied with the epsilon rate is ' + str(gamma_rate * epsilon_rate))
print('The oxygen generator rating mulitpled with the CO2 scrubber ratings is ' + str(oxygen_generator_rating * CO2_scrubber_rating))
