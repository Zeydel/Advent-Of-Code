# Magic to caculate the index
def getIndex(row, column):
    # Return the n'th triangle number
    t = (column*(column+1))/2
    # Adds the column number row-1 times
    t2 = (column*(row-1))
    # Adds another triangle number
    t3 = max(0, ((row-1)*(row-2))/2)
    return int(t+t2+t3)

# Function to quickly get the value, given an index
def getValue(index):
    return 20151125*pow(252533,index-1,33554393)%33554393

# Open input and read as words
f = open('input.txt', 'r')
presents = f.read().split(' ')

# Extract the row and column
row = int(presents[16][:-1])
column = int(presents[18][:-1])

# Find the index and find the results
index = getIndex(row, column)
print(f'The value at row {row} and column {column} is {getValue(index)}')