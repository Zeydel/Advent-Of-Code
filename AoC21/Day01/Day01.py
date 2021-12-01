# Function for finding number of increases in the measurements
def numberOfIncreases(numbers):
    increases = 0
    
    for i in range(1, len(numbers)):
        if(numbers[i] > numbers[i-1]):
            increases += 1
    return increases

# Function for finding number of sliding window increases in the measurements
def numberOfThreeIncreases(numbers):
    increases = 0
    
    for i in range(3, len(numbers)):
        if(numbers[i] > numbers[i-3]): # We only need to compare newest number and oldest number.
            increases += 1             # Other numbers are the same
    return increases

# Read input and convert to ints
f = open('input.txt', 'r')
numbers = [int(n) for n in f.read().split('\n')]

# Print results
print('There are ' + str(numberOfIncreases(numbers)) + ' increases between the measurements')
print('There are ' + str(numberOfThreeIncreases(numbers)) + ' sliding window increases in the measurements')