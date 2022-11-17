# Stuff is just easier in numpy arrays
import numpy as np

# Function to get most and least frequent letter from a list
def getMostAndLeastFrequent(letters):
    
    # A dict
    countDict = dict()
    
    # For each letter, count it
    for l in letters:
        if not l in countDict:
            countDict[l] = 0
        countDict[l] += 1
        
    # Sort it according to letter count
    sortedDict = sorted(countDict, key=lambda l: -countDict[l])
    
    # Return most and least frequent element
    return (sortedDict[0], sortedDict[-1])

# Read input as parse it as a np array
f = open('input.txt', 'r')
signals = np.array([np.array(list(l)) for l in f.read().split('\n')])

# Vars for the messages
messageMost = ''
messageLeast = ''

# For the length of the first string
for i in range(len(signals[0])):

    # Get the most and least frequent letter for that position
    most, least = getMostAndLeastFrequent(signals[0:,i])
    
    # And add them to the messages
    messageMost += most
    messageLeast += least
    
print(f'When following the repetition code, the message is {messageMost}')
print(f'When following the modified repetition code, the message is {messageLeast}')