# XOR operation
def mix(number, value):
    return number ^ value

# Modulo operation
def prune(number):
    return number % 16777216

# Given a number, follows direction to obatin next number
# in sequence
def get_new_number(number):
    
    new_number = number
    
    number = number * 64
    new_number = mix(new_number, number)
    new_number = prune(new_number)
    
    number = new_number // 32
    new_number = mix(new_number, number)
    new_number = prune(new_number)
    
    number = new_number * 2048
    new_number = mix(new_number, number)
    new_number = prune(new_number)
    
    return new_number
    
# Uses the above function n number of times to gain a new number
# also saves the first appearance of each tuple of four differences
# along with the amount of bananas obtained if selling after the sequence
def get_nth_number(number, n):
    
    first_appearances = dict()
    differences = []
    
    for _ in range(n):
        
        new_num = get_new_number(number)
                
        number_ones = int(str(number)[-1])
        new_num_ones = int(str(new_num)[-1])
        
        differences.append(new_num_ones - number_ones)
        
        if len(differences) > 3 and tuple(differences[-4:]) not in first_appearances:
            first_appearances[tuple(differences[-4:])] = new_num_ones
    
        number = new_num
        
    return number, first_appearances

# Given a sequence, return the total number of bananas we an obtain,
# if we sell after the sequence
def get_banana_count_sum(first_appearances, target):
    
    banana_sum = 0
    
    for number in first_appearances:
        
        if target in first_appearances[number]:
            
            banana_sum += first_appearances[number][target]
            
    return banana_sum

# Enumerate every possible sequence and get the best one
def get_most_bananas(number_sequences):
    
    most_bananas = 0
    
    for i in range(-9, 10):
        for ii in range(-9, 10):
            for iii in range(-9, 10):
                for iv in range(-9, 10):
                    
                    target = (i, ii, iii, iv)
                                        
                    banana_sum = get_banana_count_sum(number_sequences, target)
                    
                    if banana_sum > most_bananas:
                        most_bananas = banana_sum
                        
    return most_bananas

# open file and read as a list of numbers
file = open('input.txt', 'r')
numbers = [int(number.strip()) for number in file.readlines()]

# Init var for the sum of secret numbers
secret_number_sum = 0

# Init var for number sequences
number_sequences = dict()

# For every starting number
for number in numbers:
    
    # Get the secret number after 2000 iterations and add to result
    secret_number, first_appearances = get_nth_number(number, 2000)
    secret_number_sum += secret_number
    
    # Save the mappings of number sequences to bananas obtainde
    number_sequences[number] = first_appearances
    
# Get the most bananas we can obtain
most_bananas = get_most_bananas(number_sequences)

# Print the results
print(f'{secret_number_sum} is the sum of secret numbers after 2000 iterations')
print(f'{most_bananas} is the maximum number of bananas we can obtain')