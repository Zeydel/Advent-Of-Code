# Some spaghetti to find the signal patterns mappings
def build_map(input_values):
    
    # Sort split each signal pattern into a sorted array
    # Create a big list containing every array
    # Sort the list by length
    char_lists = sorted([sorted(i) for i in input_values], key=len)
    
    # We know these ones
    one = char_lists[0]
    four = char_lists[2]
    seven = char_lists[1]
    eight = char_lists[9]
    
    # Remove them from the list
    char_lists = char_lists[3:9]
    
    # The signal pattern for nine is the only remainging one that has complete
    # overlap with the four. Find it and remove it from the list
    nine = []
    for cl in char_lists:
        if all([f in cl for f in four]):
            nine = cl
            char_lists.remove(cl)
            break
        
    # The signal pattern for three is the only remainging one that has complete
    # overlap with the seven. Find it and remove it from the list        
    three = []
    for cl in char_lists:
        if all([s in cl for s in seven]):
            three = cl
            char_lists.remove(cl)
            break
        
    # The signal pattern for zero is the only remainging one that has complete
    # overlap with the one. Find it and remove it from the list
    zero = []
    for cl in char_lists:
        if all([o in cl for o in one]):
            zero = cl
            char_lists.remove(cl)
            break
     
    # The signal pattern for six is the only one that has six chars
    six = char_lists[2]
    char_lists.remove(char_lists[2])
    
    
    # The signal pattern for five is the only remainging one that has complete
    # overlap with the six. Find it and remove it from the list
    five = []
    for cl in char_lists:
        if all([c in six for c in cl]):
            five = cl
            char_lists.remove(cl)
            break
     
    # The final list is the signal pattern for two
    two = char_lists[0]
    
    # Join the numbers into strings and create the maps
    number_maps = {
    ''.join(zero) : 0,
    ''.join(one) : 1,
    ''.join(two) : 2,
    ''.join(three) : 3,
    ''.join(four) : 4,
    ''.join(five) : 5,
    ''.join(six) : 6,
    ''.join(seven) : 7,
    ''.join(eight) : 8,
    ''.join(nine) : 9
    }
    
    # Return the map
    return number_maps

# Open file and read as list of strings
f = open('input.txt', 'r')
entries = f.read().split('\n')

# Lengths of the easy digits, (1, 4, 7 and 8)
easy_counts = [2, 4, 3, 7]

# Init some counters
easy_count_appears = 0
hard_count_sum = 0

# For each entry
for entry in entries:
    
    # Get the output
    output = entry.split('|')[1].split()
    
    # Count the instances of digits 1, 4, 7 and 8 using the lengths
    easy_count_appears += sum([len(s) in easy_counts for s in output])
    
    # Build a map from the input
    number_maps = build_map(entry.split('|')[0].split())
    
    # Create the string using the output and the map
    digits = ''
    for o in output:
        digits += str(number_maps[''.join(sorted(o))])
      
    # Add its integer representation to the sum
    hard_count_sum += int(digits)

# Print the results
print('The digits 1, 4, 7 and 8 appear ' + str(easy_count_appears) + ' times')
print('The sum of all output values is ' + str(hard_count_sum))