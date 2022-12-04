# Parse the input into a list of tuples of sets. One set for each bag compartment
def parse(contens):
    contentList = []
        
    for c in contents:
        contentList.append((set(c[:len(c)//2]), set(c[len(c)//2:])))
        
    return contentList
            
# Get the value of a character
def getValue(char):
    if char.isupper():
        return ord(char)-38
    else:
        return ord(char)-96

# Read and parse the input
f = open('input.txt', 'r')
contents = f.read().split('\n')

# Parse the contents
contents = parse(contents)

# Init some vars
total = 0
totalBadge = 0

# For every backpack
for c in contents:
    
    # Add the value of the intersection of the two bag compartments
    total += getValue(c[0].intersection(c[1]).pop())
    
# For every set of three backpacks
for i in list(range(len(contents)))[::3]:
    
    # Find the common element using set operations
    common = (contents[i][0] | contents[i][1]).intersection(contents[i+1][0] | contents[i+1][1]).intersection(contents[i+2][0] | contents[i+2][1])
    
    # Add the value of the common element
    totalBadge += getValue(common.pop()) 

# Print the results
print(f'The sum of all common objects is {total}')
print(f'The sum of all badges is {totalBadge}')