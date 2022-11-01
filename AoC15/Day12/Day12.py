import json

# Function for summing all values in a json object containing dicts, lists and ints
def getValue(data):
    
    # Init value as zero
    value = 0
    
    # If it is a dict, sum value of all values
    if isinstance(data, dict):
        for d in data:
            value += getValue(data[d])
            
    # If it is a list, sum value of all elements
    elif isinstance(data, list):
        for d in data:
            value += getValue(d)
            
    # If it is an int, just add it
    elif isinstance(data, int):
        value += data
    return value

# Function like above, but filters out dicts where at least one of the 
# values is 'red'
def getValueWithoutRed(data):
    value = 0
    
    # Does the same as above, but returns 0 if one of the values
    # in the dict is 'red'
    if isinstance(data, dict) and 'red' not in data.values():
        for d in data:
            value += getValueWithoutRed(data[d])
    elif isinstance(data, list):
        for d in data:
            value += getValueWithoutRed(d)
    elif isinstance(data, int):
        value += data
    return value

# Open the input and read as one long string
f = open('input.txt', 'r')
jsonString = f.read()

# Deserialise the data
data = json.loads(jsonString)

# Print the results
print(f'The sum of all numbers in the object is {getValue(data)}')
print(f'The sum of all numbers in the object, excluding red numbers, is {getValueWithoutRed(data)}')