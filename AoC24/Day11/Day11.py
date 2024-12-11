# Take the input and make a dictionary of the stones and their counts
def get_initial_arrangement(stones):

    # Init empty dict
    stone_dict = dict()
        
    # For every stone
    for stone in stones:
        
        # Init it in the dict if we haven't seen it before
        if stone not in stone_dict:
            stone_dict[stone] = 0
        
        # Incement count
        stone_dict[stone] += 1
        
    # Return the dict
    return stone_dict
        
# Get stones after blinking
def blink(stones):
    
    # Init new dict
    new_stones = dict()
    
    # For every stone
    for stone in stones:
        
        # Init list of stones to add
        to_add = []
        
        # If stone is zero, we want to add a one
        if stone == 0:
            to_add.append(1)
            
        # If stone lenght is even, split the number into two and add both
        # halves to list
        elif len(str(stone)) % 2 == 0:
            
            stone_string = str(stone)
            
            to_add.append(int(stone_string[len(stone_string)//2:]))
            to_add.append(int(stone_string[:len(stone_string)//2]))
            
        # Otherwise add the value of the stone multiplied by 2024
        else:
            to_add.append(stone * 2024)
            
        # Add the stones to add
        for add in to_add:
            
            if add not in new_stones:
                new_stones[add] = 0
                
            new_stones[add] += stones[stone]
            
    return new_stones

# Sum the stones in the dictionary
def get_stone_count(stones):
    
    count = 0
    
    for stone in stones:
        
        count += stones[stone]
        
    return count

# Open file and read as list of numbers
file = open('input.txt', 'r')
stones = [int(num) for num in file.readline().split()]

# Get initial arrangement of stones as dict
stones = get_initial_arrangement(stones)

# Init number of blinks
num_blinks = 25

# Blink a lot
for i in range(num_blinks):
    stones = blink(stones)
    
# Get the stone count
stone_count_25 = get_stone_count(stones)

# Init new number of blinks
num_blinks = 50

# Blink even more
for i in range(num_blinks):
    stones = blink(stones)
    
# Get the new stone counts
stone_count_50 = get_stone_count(stones)

# Print the results
print(f'{stone_count_25} is the number of stones after 25 blinks')
print(f'{stone_count_50} is the number of stones after 50 blinks')