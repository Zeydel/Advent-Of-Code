# Function to get the lower bound of possible times, given a total time and a record to beat
def get_lower_bound(time, record, low=0, high=-1):
       
    # If high is uninitialised, set it to the max value
    if high == -1:
        high = time
    
    # Take the middle value
    cur = (high+low)//2
    
    # If we have converged on a number, return it
    if low == high:
        return high
    
    # If we have converged on two numbers, check if the lower number is a winner
    if high - 1 == low:
        if get_dists(time, low) > record: # If so, return it
            return low
        else:
            return high # Else return the high number
        
    # If the current number is a winner, recurse left. Else recurse right
    if get_dists(time, cur) > record:
        return get_lower_bound(time, record, low=low, high=cur)
    else:
        return get_lower_bound(time, record, low=cur, high=high)
    
# Function to find the upper bound of the winning number. Excactly the same logic as above
def get_higher_bound(time, record, low=0, high=-1):
    
    if high == -1:
        high = time
        
    cur = (high+low)//2

    if low == high:
        return low
    
    if high - 1 == low:
        if get_dists(time, high) > record:
            return high
        else:
            return low
    
    if get_dists(time, cur) > record:
        return get_higher_bound(time, record, low=cur, high=high)
    else:
        return get_higher_bound(time, record, low=low, high=cur)

# Function to get distance traveled given a time and a press duration
def get_dists(time, press):
    return (time-press)*press

# Read and parse the input
f = open('input.txt', 'r')
records = f.read().split('\n')

# Read times and sitances as lists
times = [int(t) for t in records[0].split(':')[1].split()]
distances = [int(t) for t in records[1].split(':')[1].split()]

# Convert to individual numbers
time = int(''.join([str(t) for t in times]))
distance = int(''.join([str(d) for d in distances]))

# Init numbers for the results
winProduct = 1
winPresses = 0

# Calculate for individual numbers, and take the product
for t, d in zip(times, distances):
    
    winProduct *= (get_higher_bound(t, d) + 1) - get_lower_bound(t, d)
    
# Calculate for single number
winPresses = (get_higher_bound(time, distance) + 1) - get_lower_bound(time, distance)

# Print the results
print(f'The product of the number of winning presses is {winProduct}')
print(f'There are {winPresses} diffrent ways to win')