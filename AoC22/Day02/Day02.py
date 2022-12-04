# Get the score using the first interpretation of the strategy
def getScore(strategy):
    
    # Init as zero
    totalScore = 0
    
    # For every line
    for s in strategy:
        
        # If it is a win or a draaw, add some points
        if s in wins:
            totalScore += 6
        elif s in draws:
            totalScore += 3
            
        # Add the points of the hand
        totalScore += scores[s.split()[1]]
        
    return totalScore

# Get the score for the correct interpretation of the strategy
def getScoreCorrecct(strategy):
    totalScore = 0
    
    # For every line, add the strategy value
    for s in strategy:
        totalScore += correctScores[s]
        
    return totalScore
        

# Read and parse the input
f = open('input.txt', 'r')
strategy = f.read().split('\n')

# Hand values
scores = {
    'X':1,
    'Y':2,
    'Z':3
    }

# Sets of wins and draws
wins = {'A Y', 'B Z', 'C X'}
draws = {'A X', 'B Y', 'C Z'}

# Score for every combination of hands
correctScores = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
        }

# Print the results
print(f'The score of the strategy is {getScore(strategy)}')
print(f'The score of the correct interpretation of the strategy is {getScoreCorrecct(strategy)}')