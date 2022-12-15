# Parse the data into dicts of sensors and their nearest beacon
def parse(data):
    
    sensors = dict()
    
    for d in data:
        
        d = d.split(' ')
        
        sX = int(d[2].split('=')[1].strip(','))
        sY = int(d[3].split('=')[1].strip(':'))
        
        bX = int(d[8].split('=')[1].strip(','))
        bY = int(d[9].split('=')[1])
        
        sensors[(sX, sY)] = (bX, bY)
        
    return sensors

# Manhatten distance between two points
def getDistance(p1, p2):
    
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# For a single row, get the set of points where there cannot be a beacon
def getExclusionsRow(sensors, y):
    
    exclusions = set()
    
    # For every sensor
    for s in sensors:
        sy = abs(s[1]-y)
        d = getDistance(s, sensors[s])
            
        # Compute the set of x coordinates where there cannot be a beacon
        exclusions |= set([x for x in range((s[0]-d)+abs(sy), (s[0]+d+1)-abs(sy))])
    
    return exclusions

# Open input and read as strings
f = open('input.txt', 'r')
data = f.read().split('\n')

# Parse the data
sensors = parse(data)

# Find all the points where there cannot be a sensor
y = 10
exclusions = getExclusionsRow(sensors, y)

# Remove all the points that contain a sensor
for s in sensors:
    
    if sensors[s][1] == y and sensors[s][0] in exclusions:
        exclusions.remove(sensors[s][0])

# Save the length
exclusionsRow = len(exclusions)

# Problem variables
lim = 4000000
frequency = -1
x, y = 0, 0
found = False

# Create a dict of closest distances to each sensor
closestDists = dict()
for s in sensors:
    closestDists[s] = getDistance(s, sensors[s])

# Sort the keys by descending x value
sensors = sorted(sensors, key=lambda se: -se[0])

# While frequency is not found
while True:
    
    # Assume we have found a spot
    found = True
    
    # For every sensor
    for s in sensors:
        
        # If there cannot be a sensor
        if getDistance(s, (x, y)) <= closestDists[s]:
            found = False
            
            # Move x to outside the signals range and break
            x = s[0]+(closestDists[s]-abs(s[1]-y))
            break
    
    # If we have found a result, compute the frequency and break
    if found:
        frequency = x*4000000 + y
        break
            
    # If x is inside the limit, increment
    if x <= lim:
        x += 1
        
    # Else reset x and increment y
    else:
        x = 0
        y += 1

# Print the results
print(f'On row 2000000, {exclusionsRow} points cannot contain a beacon')
print(f'The frequency is {frequency}')