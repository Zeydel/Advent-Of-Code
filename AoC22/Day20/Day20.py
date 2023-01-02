# Function to mix numbers according to ordering
def mixWithOrdering(numbers, ordering):
    
    # Create a copy of the lsit
    mixed = list(numbers)
    
    # List to store the new ordering
    newOrdering = []
    
    # For the length of the ordering
    for i in range(len(ordering)):
        
        # Get the index
        cur_idx = ordering[i]
        
        # Get the item
        n = mixed[cur_idx]
            
        # Delete it
        del mixed[cur_idx]
        
        # Find out where its supposed to be
        new_idx = (n + cur_idx) % (len(mixed))
        
        # Insert it
        mixed.insert(new_idx, n)

        # For every element in the new ordering
        for j, o in enumerate(newOrdering):
            
            if o > cur_idx and o > new_idx:
                continue
            if o < cur_idx and o < new_idx:
                continue
            
            # Adjust indices
            if o > cur_idx and o <= new_idx:
                newOrdering[j] -= 1
            if o < cur_idx and o >= new_idx:
                newOrdering[j] += 1
        
        # Add the index to the new ordering
        newOrdering.append(new_idx)
        
        # Repeat the above for current ordering
        for j, o in enumerate(ordering[i:]):
            
            if o > cur_idx and o > new_idx:
                continue
            if o < cur_idx and o < new_idx:
                continue
            
            if o > cur_idx and o <= new_idx:
                ordering[j+i] -= 1
            if o < cur_idx and o >= new_idx:
                ordering[j+i] += 1
        
    # Return the mixed numbers and the new ordering
    return (mixed, newOrdering)


# Open input and read as strings
f = open('input.txt', 'r')
numbers = [int(i) for i in f.read().split('\n')]

# Init ordering as sequential
ordering = [i for i in range(len(numbers))]

# Mix numbers
mixed, _ = mixWithOrdering(numbers, ordering)
    
# Find the zero
zeroPlace = -1
for i in range(len(mixed)):
    
    if mixed[i] == 0:
        zeroPlace = i
        break

# Get the coordinate
coordinates = mixed[(zeroPlace + 1000)%len(mixed)] + mixed[(zeroPlace + 2000)%len(mixed)] + mixed[(zeroPlace + 3000)%len(mixed)]

# Apply the secret key
numbers = [i*811589153 for i in numbers]

# Create a new sequential ordering
ordering = [i for i in range(len(numbers))]

# Do 10 times
for i in range(10):
    
    # Get the numbers and a new ordering
    numbers, ordering = mixWithOrdering(numbers, ordering)
        
    
# Find the new zero
for i in range(len(numbers)):
    
    if numbers[i] == 0:
        zeroPlace = i
        break

# Find the new coordinate
longCoordinates = numbers[(zeroPlace + 1000)%len(numbers)] + numbers[(zeroPlace + 2000)%len(numbers)] + numbers[(zeroPlace + 3000)%len(numbers)]

print(f'The coordinate is {coordinates}')
print(f'Using the secret key, the coordinate is {longCoordinates}')