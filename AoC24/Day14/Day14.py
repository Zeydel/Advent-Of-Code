# Parse the input lines into a list of robots
def parse(lines):
    
    robots = []
    
    for line in lines:
        
        p, v = line.split(' ')
        
        p = p.split('=')[1].split(',')
        
        point = (int(p[0]), int(p[1]))
    
        v = v.split('=')[1].split(',')
        
        velocity = (int(v[0]), int(v[1]))

        robots.append((point, velocity))
        
    return robots

# Get position of a robot after a number of seconds
def get_position_after_seconds(robot, seconds, max_x, max_y):
    
    # Split info into initial position and velocity
    position, velocity = robot
    
    # Use math to get position after number of seconds
    new_x = (position[0] + (velocity[0] * seconds)) % max_x
    new_y = (position[1] + (velocity[1] * seconds)) % max_y
    
    # Return the new position
    return (new_x, new_y)

# Get safety score of robots
def get_safety_score(positions, max_x, max_y):
    
    # We count the number of robots in each quadrant
    robots = [0, 0, 0, 0]
    
    # For each position, figure out the quadrant and add to score
    for x, y in positions:
        
        if x < max_x // 2 and y < max_y // 2:
            robots[0] += 1
        elif x < max_x // 2 and y > max_y // 2:
            robots[1] += 1
        elif x > max_x // 2 and y < max_y // 2:
            robots[2] += 1
        elif x > max_x // 2 and y > max_y // 2:
            robots[3] += 1
    
    return robots[0] * robots[1] * robots[2] * robots[3]
    
# Find out if there is a christmas tree in the map
# based on a lot of assumptions that may not be true
def is_connected(positions):
        
    # We do a series of group searches. Init direstions we can search in
    dirs = []
    
    for x in range(-1, 2):
        for y in range(-1, 2):
            dirs.append((x, y))
    
    # Init list for groups sizes
    group_sizes = []
    
    # Take positions as a set
    positions = set(positions)
    
    # We are looking for a group of over 100 robots next to each other
    # if there are fewer than 100 robots left to explore, we can quit
    while len(positions) > 100:
    
        # Make a search queue and pop a random robot into it
        queue = []
        queue.append(positions.pop())
    
        # Init the size of the group
        group_size = 1
    
        # Explore and count group size
        while len(queue) > 0:
        
            x, y = queue.pop()
        
            for dx, dy in dirs:
                if (x + dx, y + dy) in positions:
                    positions.remove((x + dx, y + dy))
                    queue.append((x + dx, y + dy))
                    group_size += 1

        # Once there is nothing left to explore, add the group
        # size to the list
        group_sizes.append(group_size)
    
    # If we have found a group of size over 100, return True
    for group_size in group_sizes:
        if group_size > 100:
            return True
        
    # Otherwise return false
    return False

# Print the robots
def print_robots(positions, max_x, max_y):
        
    for y in range(max_y):
        for x in range(max_x):
            
            char = '.'
            
            if (x, y) in positions:
                char = '#'
                
            print(char, end='')
           
        print()
    print()

    
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
robots = parse(lines)

# Init map bounds
max_x = 101
max_y = 103

# Empty list to store the robots after 100 seconds
positions_after_100_seconds = []

# Calculate positions adter 100 seconds
for robot in robots:
    positions_after_100_seconds.append(get_position_after_seconds(robot, 100, max_x, max_y))
    
# Get score
safety_score = get_safety_score(positions_after_100_seconds, max_x, max_y)

# Search for when the christmas tree appeas
seconds = 0
while True:
    
    seconds += 1
    
    positions = []
    
    for robot in robots:
        positions.append(get_position_after_seconds(robot, seconds, max_x, max_y))
        
    # Break when we find the tree
    if is_connected(positions):
        # Remove # to see the tree
        print_robots(positions, max_x, max_y)
        break

# Print the results
print(f'{safety_score} is the safety score')
print(f'{seconds} is the first number of seconds where the christmas tree appears')