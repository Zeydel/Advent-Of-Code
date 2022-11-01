# Function to find the square feet of paper needed to wrap a present, given
# the dimensions in an array
def getPaperNeededForPresent(d):
    return 2*d[0]*d[1] + 2*d[1]*d[2] + 2*d[2]*d[0] + (sorted(d)[0]*sorted(d)[1])

# Function to find the feet of ribbon needed to wrap a present, given
# the dimensions in an array
def getRibbonNeededForPresent(d):
    return 2*sorted(d)[0] + 2*sorted(d)[1] + d[0]*d[1]*d[2]

# Gets the total paper needed for to wrap every present
def getTotalPaperNeeded(dimensionList):
    sqrFeet = 0
    
    for d in dimensions:
        sqrFeet += getPaperNeededForPresent([int(n) for n in d.split('x')])
        
    return sqrFeet

# Gets the total ribbon needed to wrap every present
def getTotalRibbonNeeded(dimensionList):
    feet = 0
    
    for d in dimensions:
        feet += getRibbonNeededForPresent([int(n) for n in d.split('x')])
        
    return feet

# Read input as list of lines
f = open('input.txt', 'r')
dimensions = f.read().split('\n')

# Prints the result
print(f'{getTotalPaperNeeded(dimensions)} square feet of paper is needed for the presents')
print(f'{getTotalRibbonNeeded(dimensions)} feet of ribbon is needed for the presents')