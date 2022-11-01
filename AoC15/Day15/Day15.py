# Oarses the strings into a list of tuples, representing the properties of the
# different ingredients
def parse(strings):
    
    # Init empty list
    properties = []
    
    # For every string
    for s in strings:
        
        # Split it, and add the values to a tuple
        split = [sp.strip(',') for sp in s.split()]
        properties.append((int(split[2]), int(split[4]), int(split[6]), int(split[8]), int(split[10])))
        
    # Return the list
    return properties

# Generates all choices, given a number of ingredients and a spoons capacity
def generateChoices(length, spoons, prev = None):
    
    # Initially empty list of choices
    choices = []
    
    # If we dont have a current choice, create an empty one
    if prev == None:
        prev = []
    
    # Copy that
    choice = prev.copy()
    
    # If there is only one number left to add, we can calculate it.
    # Do that, add it to an array and return it.
    if length == 1:
        choice.append(spoons)
        choices.append(choice)
        return choices
    
    # Otherwise we have multiple choices for the remaining numbers.
    # Add a placeholder
    choice.append(-1)
    
    # For every possible remaining number in that place
    for i in range(0, spoons+1):
        
        # Try that number
        choice[-1] = i
        
        # And compute all choices for the rest of the array. Add that
        # to the output
        choices += generateChoices(length-1, spoons-i, choice)
        
    # Return the choices
    return choices

# Gets the value for a given selection of ingredients
def getChoiceValue(choice, ingredients):
    
    # Init as 1 (we are gonna be multiplying)
    choiceval = 1
    
    # For every property
    for i in range(len(ingredients[0])-1):
        
        # Initially zero
        propval = 0
        
        # For every ingredient
        for c, j in enumerate(ingredients):
            
            # Add the number og spoons for that ingredient times the
            # value for that property
            propval += choice[c] * j[i]
            
        # Limit by zero
        if propval < 0:
            propval = 0
            
        # Multiply the property value
        choiceval *= propval
        
    # And return the value
    return choiceval

# Gets the calorie count for a given choice
def getCalorieValue(choice, ingredients):
    
    # Init as zero
    calories = 0
    
    # Adds the calorie values for the given choice
    for c, i in enumerate(ingredients):
        calories += choice[c] * i[-1]
        
    return calories

# Read as strings
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Parse the input and generate all the choices
ingredients = parse(strings)
choices = generateChoices(4, 100)

# Init vars for best results
best = 0
bestWith500Calories = 0

# For every choice
for c in choices:
    
    # Compute value and calorie count
    val = getChoiceValue(c, ingredients)
    calories = getCalorieValue(c, ingredients)
    
    # If we beat the record, store it
    if val > best:
        best = val
        
    # If the calorie count is 500, and we beat the record, store it
    if val > bestWith500Calories and calories == 500:
        bestWith500Calories = val
        
# Print the results
print(f'The best possible value is {best}')
print(f'The best possible value with 500 calories is {bestWith500Calories}')


