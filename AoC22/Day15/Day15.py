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

def getDistance(p1, p2):
    
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def getBounds(sensors):
    
    xMin, xMax = float('inf'), float('-inf')
    yMin, yMax = float('inf'), float('-inf')
    
    for s in sensors:
        d = getDistance(s, sensors[s])
        
        if s[0] + d > xMax:
            xMax = s[0] + d
        if s[0] - d < xMin:
            xMin = s[0] - d
        if s[1] + d > yMax:
            yMax = s[1] + d
        if s[1] - d < yMin:
            yMin = s[1] - d
    
    return (xMin, xMax, yMin, yMax)

def canBeBeacon(x, y):
    
    for s in sensors:
        
        if sensors[s] == (x,y):
            return True
        
        if getDistance(s, sensors[s]) >= getDistance(s, (x, y)):
            return False
        
    return True

def getBeaconPos(maxC):
    
    for x in range(maxC):
        for y in range(maxC): 
    

# Open input and read as strings
f = open('input.txt', 'r')
data = f.read().split('\n')

sensors = parse(data)
xMin, xMax, yMin, yMax = getBounds(sensors)

notBeaconCounter = 0
y = 2000000

for x in range(xMin, xMax+1):
    
    if not canBeBeacon(x, y):
        notBeaconCounter += 1
        
print(notBeaconCounter)