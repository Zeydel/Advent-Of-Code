# Check if game is possible given a number of marbles of each color
def is_possible(game, marble_count):
    
    # For every round in the game
    for rnd in game:
        
        # For every set of marbles drawn
        for marbles in rnd.split(', '):
            number, color = marbles.split(' ')
            
            # If the draw was not possible, return false
            if int(number) > marble_count[color]:
                return False
            
    # If we havent been able to prove it false, return true
    return True

# Get the power number of a game
def get_power(game):
    
    # Init a var for each color
    marble_count = {'red': 0,
                    'green': 0,
                    'blue': 0}
    
    # For every round in the game
    for rnd in game:
        
        # For every set of marbles drawn
        for marbles in rnd.split(', '):
            number, color = marbles.split(' ')
            
            # If current draw has more marbles than the saved number, update it
            if marble_count[color] < int(number):
                marble_count[color] = int(number)
            
    # Return the product of the marble counts
    return marble_count['red'] * marble_count['green'] * marble_count['blue']

# Vars for the number of marbles
marble_count = {'red': 12,
                'green': 13,
                'blue': 14
                }

# Read and parse the input
f = open('input.txt', 'r')
games = f.read().split('\n')

# Do a bit of preprocessing
games = [g.split(': ')[1] for g in games]
games = [g.split('; ') for g in games]

# Vars for the result
possible_sum = 0
power_sum = 0

# For every game, determine whether it is possible and calculate the power
for i, game in enumerate(games):
    
    if is_possible(game, marble_count):
        possible_sum += i+1
        
    power_sum += get_power(game)
    
# Print the results
print(f'The sum of indices of possible games is {possible_sum}')
print(f'The sum of powers of the games is {power_sum}')