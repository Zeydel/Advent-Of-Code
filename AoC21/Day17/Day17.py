# Function to check whether the current location is in target
def is_in_target(target_min_x, target_max_x, target_min_y, target_max_y, p_x, p_y):
    if target_min_x <= p_x and p_x <= target_max_x and target_min_y <= p_y and p_y <= target_max_y:
        return True
    return False

# Function to update position and velocity
def get_next_pos_and_vel(v_x, v_y, p_x, p_y):
    p_x += v_x
    p_y += v_y
    
    if v_x > 0:
        v_x -= 1
    elif v_x < 0:
        v_x += 1
        
    v_y -= 1
    
    return (v_x, v_y, p_x, p_y)

# Function to check if we have gone to far, and is no longer able to hit the target
def has_missed(target_max_x, target_min_y, p_x, p_y):
    return p_x > target_max_x or p_y < target_min_y

# Function to check whether we will hit the target given a velocity
def does_hit(target_min_x, target_max_x, target_min_y, target_max_y, v_x, v_y):
    
    # Start at 0,0
    p_x, p_y  = 0, 0
    
    # Maximum y position
    max_y_pos = 0
    
    # While we have not gone too far
    while not has_missed(target_max_x, target_min_y, p_x, p_y):
        
        # If we are at a new max y position, update the max
        if p_y > max_y_pos:
            max_y_pos = p_y
        
        # If we are at the target, return the max position
        if is_in_target(target_min_x, target_max_x, target_min_y, target_max_y, p_x, p_y):
            return max_y_pos
        
        # Update position and velocity
        (v_x, v_y, p_x, p_y) = get_next_pos_and_vel(v_x, v_y, p_x, p_y)
        
    # If we have missed the target entirely, return -1
    return -1
    
# Function to get the best initial velocity
def find_best_initial_velocity(target_min_x, target_max_x, target_min_y, target_max_y):
    
    # Counter number of misses
    miss_counter = 0
    
    # Highest found peak
    peak = -1
    
    # Current value of y velocity
    v_y = 0
    
    while True:
                
        # For every x between zero and maximum target x
        for v_x in range(target_max_x):
            
            # Find out if this combination of x and y hits the target
            cur_peak = does_hit(target_min_x, target_max_x, target_min_y, target_max_y, v_x, v_y)
            
            # We did not hit, go to next iteration
            if cur_peak == -1:
                continue
            
            # If we did hit the target, and the peak was higher than previosly found peak, update it
            if cur_peak > peak:
                peak = cur_peak
                break
                
        # If current y value didn't work, increment miss counter
        if cur_peak == -1:
            miss_counter += 1
        else:
            miss_counter = 0
            
        # If we have missed 25 times in a row, we are probably not going to find anymore. Exit the loop
        if miss_counter == 25:
            break
        
        # Increment y
        v_y += 1
            
    # Return the best found peak
    return peak
         
# Function to find all initial velocities that hits the target   
def find_all_initial_velocities(target_min_x, target_max_x, target_min_y, target_max_y):
    
    # Set of velocities
    velocities = set()
    
    # Count the number of misses
    miss_counter = 0
    
    # Start possible y coordinates at lowest target y
    v_y = target_min_y
    
    while True:
    
        # Var to check if have hit anything with the current y value
        hit = False
        
        # For every possible x value
        for v_x in range(target_max_x+1):
            
            # Find out if we hit the target
            cur_peak = does_hit(target_min_x, target_max_x, target_min_y, target_max_y, v_x, v_y)
            
            # If we didn't, go to next iterations
            if cur_peak == -1:
                continue
            
            # Add the current velocity to the set and mark that we hit the target
            velocities.add((v_x, v_y))
            hit = True
                
        # If we did not hit, increse the miss counter
        if not hit:
            miss_counter += 1
        else:
            miss_counter = 0
            
        # If we have missed 25 times in a row, exit the loop
        if miss_counter == 25:
            break
        
        # Increment y velocity
        v_y += 1
            
    # return the set of velocities
    return velocities    
    

# Open file and read as one string
f = open('input.txt', 'r')
target = f.read()

# Parse the target coordinates into integers
min_x, max_x = [int(i) for i in target.split(' ')[2].split('=')[1][:-1].split('..')]
min_y, max_y = [int(i) for i in target.split(' ')[3].split('=')[1].split('..')]

print('The highest possible y position is ' + str(find_best_initial_velocity(min_x, max_x, min_y, max_y)))
print('The number of coordinates that hit the target is ' + str(len(find_all_initial_velocities(min_x, max_x, min_y, max_y))))