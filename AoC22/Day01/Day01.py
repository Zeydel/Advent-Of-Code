# Function to get total calories for every elf
def getElfCalories(elves):
    
    # Init empty list
    calories = []
    
    # For every elf, sum up its calories and add to list
    for e in elves:
        calories.append(sum([int(s) for s in e.splitlines() ]))
                    
    # Return the sorted descending list
    return sorted(calories, key=lambda c: -c)

# Read and parse the input
f = open('input.txt', 'r')
elves = f.read().split('\n\n')

# Get the calories carried by each elf
calories = getElfCalories(elves)

# Print the result
print(f'The top elf is carrying {calories[0]} calories')
print(f'The top three elves are carrying a total of {sum(calories[0:3])} calories')