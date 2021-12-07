# Function to get the n'th triange number
def get_cost(number):
    return int((number*(number+1))/2)

# Open file and read as list og integers
f = open('input.txt', 'r')
numbers = [int(i) for i in f.read().split(',')]

# Init variables to store the results. Set as max value to start
min_fuel = float('inf')
min_fuel_part_2 = float('inf')

# For each number
for n in numbers:
    
    # Calculate the total fuel cost to align crabs using both measures
    fuel_usage = sum([abs(x-n) for x in numbers])
    fuel_usage_part_2 = sum([get_cost(abs(x-n)) for x in numbers])

    # Update values if we have found a new best value
    if fuel_usage < min_fuel:
        min_fuel = fuel_usage
        
    if fuel_usage_part_2 < min_fuel_part_2:
        min_fuel_part_2 = fuel_usage_part_2
    
# Print the values
print('The minimum amount of fuel to spend using the first measure is ' + str(min_fuel))
print('The minimum amount of fuel to spend using the second measure is ' + str(min_fuel_part_2))