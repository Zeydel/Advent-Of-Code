# Array operations
import numpy as np

# Parses the input into a list of tuples. Each tuple represents reindeer
def parse(strings):
    
    # Empty list of reindeer
    reindeer = []
    
    # For every string
    for s in strings:
        
        # Split it
        split = s.split(' ')
        
        # Read           SPEED         FLYING DURATION  REST DURATION
        reindeer.append((int(split[3]), int(split[6]), int(split[13])))
    
    # Return the list of reindeer
    return reindeer

# Gets the distance travelled after some time
def getDistanceTravelled(time, speed, duration, rest):
    
    # Initially 0
    dist = 0
    
    # Find out how many complete fly-rest cycles we can do
    rounds = int(time/(duration+rest))
    
    # Add that to the distance
    dist += rounds*(speed*duration)
    
    # Substract the needed time
    time -= rounds*(duration+rest)
    
    # If we have less time left than a fly, add the remaining flying time
    if time < duration:
        dist += time*speed
    
    # If we can perform a full fly, add that
    else:
        dist += duration*speed
        
    # Return the dist
    return dist

# Function to get the score of the best reindeer
def getBestScore(reindeer, rounds):
    
    # Arrays for keeping track of the scores and distances
    dist = np.zeros(len(reindeer), dtype = int)
    score = np.zeros(len(reindeer), dtype = int)
    
    # For every round
    for t in range(1, rounds+1):
        
        # For every reindeer
        for i, r in enumerate(reindeer):

            # Calculate the reindeers current distance
            dist[i] = getDistanceTravelled(t, r[0], r[1], r[2])
            
        # For every reindeer in the lead, add one to the score
        for i in [i for i, j in enumerate(dist) if j == max(dist)]:
            score[i] += 1
            
    # Return the maximum score
    return max(score)
        

# Read as strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Parse the input
reindeer = parse(strings)

# Set up some data
rounds = 2503
bestDistance = 0

# Compute the distance for every reindeer after the race
for r in reindeer:
    distance = getDistanceTravelled(rounds, r[0], r[1], r[2])
    
    if distance > bestDistance:
        bestDistance = distance
      
# Compute the best score
bestScore = getBestScore(reindeer, rounds)
        
# Print the results
print(f'After {rounds} rounds, the best distance is {bestDistance}')
print(f'After {rounds} rounds, the best score is {bestScore}')