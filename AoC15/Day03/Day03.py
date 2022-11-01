# Gets the number of houses visited, given directions as a long string
def getNumberOfHousesThatGetPresent(directions):
    # Start santa at origo and deliver first present
    x, y = 0, 0
    houses = {(x,y)}
    
    # For each direction, move santa once and add a location to the set
    for d in directions:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '<':
            x -= 1
        elif d == '>':
            x += 1
        houses.add((x,y))
        
    # Return the size of the set
    return len(houses)

# Gets the number of houses visited, given directions as a long string
# Also counts for robosanta
def getNumberOfHousesThatGetPresentsWithRoboSata(directions):
    # Start santa and robosanta at orgio and deliver first present
    x,y,rx,ry = 0, 0, 0, 0
    houses = {(0,0)}
    
    # For each direction, move either santa or robosanta and add their location
    # to the set
    for c, d in enumerate(directions):
        if c % 2 == 0:
            if d == '^':
                y += 1
            elif d == 'v':
                y -= 1
            elif d == '<':
                x -= 1
            elif d == '>':
                x += 1
            houses.add((x,y))
        else:
            if d == '^':
                ry += 1
            elif d == 'v':
                ry -= 1
            elif d == '<':
                rx -= 1
            elif d == '>':
                rx += 1
            houses.add((rx,ry))
          
    # Return the size of the set
    return len(houses)

# Read the input as one long string
f = open('input.txt', 'r')
directions = f.read()

print(f'{getNumberOfHousesThatGetPresent(directions)} houses gets presents delivered by santa')
print(f'{getNumberOfHousesThatGetPresentsWithRoboSata(directions)} houses gets presents delivered by santa and robosanta')