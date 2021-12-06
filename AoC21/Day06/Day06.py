# Open input and read as list of numbers
f = open('input.txt', 'r')
numbers = [int(i) for i in f.read().split(',')]

# Init containers for fish
fish = [0] * 9

# Sort input fish into containers
for n in numbers:
    fish[n] += 1

# Init some variables for the loop
fish_after_80_days = -1    
days = 256

# Every day
for i in range(days):
    
    # If we are at day 80, count the number of fish
    if i == 80:
        fish_after_80_days = sum(fish)
    
    # Counter the number of fish about to create another fish
    zeros = fish[0]
    
    # Move all fish one container down
    for j in range(1, len(fish)):
        fish[j-1] = fish[j]
        
    # Add the fish that just created another fish to container 6
    fish[6] += zeros
    
    # Add the newly created fish to container 8
    fish[8] = zeros
    
# Print the results
print('The number of fish after 80 days is ' + str(fish_after_80_days))
print('The number of fish after 256 days is ' + str(sum(fish)))
