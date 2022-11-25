# Parse the string into an array of bool
def parse(rowString):
    
    # True if it is a trap. False otherwise
    row = [True if i == '^' else False for i in rowString]
    
    # Pad with fictional safe tiles
    return [False] + row + [False]

# Returns if the tile is a trap, given the relevant tiles from last round
def isTrap(prev):
    if prev[0] != prev[1] and prev[0] != prev[2]:
        return True
    if prev[2] != prev[1] and prev[2] != prev[0]:
        return True
    return False

# Generate the next row of tiles
def getNextRow(row):
    
    # Start with the fictional safe tile
    nextRow = [False]
    
    # For every real tile
    for i in range(1, len(row)-1):
        # Find out if it is a trap and add it to the row
        nextRow.append(isTrap(row[i-1:i+2]))
        
    # End with another fictional tile
    nextRow.append(False)
    
    # Return the newly generated row
    return nextRow

# Read and parse the input
f = open('input.txt', 'r')
rowString = f.read()
row = parse(rowString)

# Counter for safe tiles after 40 rounds
safeTilesAfter40 = 0

# For 40 iterations
for i in range(40):
    # Add the number of safe tiles to the counter
    safeTilesAfter40 += (len(row)-2) - sum(row)
    # Generate the next row
    row = getNextRow(row)
    
# Restore the first row
row = parse(rowString)

# Counter for safe tiles after 400000 iterations
safeTilesAfter400000 = 0

# For 400000 iterations, do the same as above
for i in range(400000):
    safeTilesAfter400000 += (len(row)-2) - sum(row)
    row = getNextRow(row)

# Print the results
print(f'After 40 rounds there are {safeTilesAfter40} safe tiles')
print(f'After 400000 rounds there are {safeTilesAfter400000} safe tiles')
#Too low 20000532