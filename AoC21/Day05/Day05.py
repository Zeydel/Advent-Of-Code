import numpy as np

# Function to get an inclusive range of two unsorted numbers
def inclusive_range(n1, n2):
    if n1 > n2:
        return range(n1, n2-1, -1)
    else:
        return range(n1, n2+1)

# Get input and split into lines
f = open('input.txt', 'r')
lines = f.read().split('\n')

# Create the two fields
field_one = np.zeros((1000,1000), dtype=int)
field_two = np.zeros((1000,1000), dtype=int)

# For each input line
for l in lines:
    
    # Get the coordinates
    coordinates = l.split(' -> ')
    x1, y1 = [int(c) for c in coordinates[0].split(',')]
    x2, y2 = [int(c) for c in coordinates[1].split(',')]
    
    # If the line is horizontal or vertical
    if x1 == x2 or y1 == y2:
        
        # Go add one to each value on line
        for i in inclusive_range(x1, x2):
            for j in inclusive_range(y1, y2):
                field_one[i][j] += 1
                field_two[i][j] += 1
    # Else line is diagonal. Add one to each value on line
    else:
        for i, j in zip(inclusive_range(x1, x2), inclusive_range(y1, y2)):
            field_two[i][j] += 1
        
# Count the overlaps in each fields
overlaps_one = 0
overlaps_two = 0
for i in range(len(field_one)):
    for j in range(len(field_one)):
        if field_one[i][j] > 1:
            overlaps_one += 1
        if field_two[i][j] > 1:
            overlaps_two += 1
            
            
print('The number of overlaps when only using vertical and horizontal lines is ' + str(overlaps_one))
print('The number of overlaps when using all lines ' + str(overlaps_two))