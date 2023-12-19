# Function to get hash value of a word
def get_hash(word):
    
    value = 0
    
    for c in word:
        value += ord(c)
        value *= 17
        value %= 256
        
    return value
    
# Function to get focus power, given the contents of boxes
def get_focus_power(boxes):
    
    focus_power = 0
    
    for boxNumber in boxes:
        
        for i, l in enumerate(boxes[boxNumber]):
            
            focus_power += (boxNumber+1) * (i+1) * l[1]
            
    return focus_power
            
# Remove a lens from a box, if present, given a word
def remove_lens(boxes, word):
    
    # Get the label and compute the hash value
    label = word[:-1]
    labelVal = get_hash(label)
    
    # If the box doesn't exist, return
    if not labelVal in boxes:
        return
    
    # Go through the lenses in the box.
    for i in range(len(boxes[labelVal])):
        
        # If we find the lens, remove it
        if boxes[labelVal][i][0] == label:
            boxes[labelVal] = boxes[labelVal][:i] + boxes[labelVal][i+1:]
            return
      
# Function to add a lens to a box, given a word
def add_lens(boxes, word):
    
    # Get the label, hash value and lens from the input
    label = word[:-2]
    labelVal = labelVal = get_hash(label)
    lens = int(word[-1])
    
    # If we havent created the box yet, do so
    if not labelVal in boxes:
        boxes[labelVal] = []
        
    # Go through the lenses in the boxes
    for i in range(len(boxes[labelVal])):
        
        # If we find a lens with the same lebal replace it
        if boxes[labelVal][i][0] == label:
            boxes[labelVal][i] = (label, int(lens))
            return
        
    # Add the lens to the box
    boxes[labelVal].append((label, int(lens)))
    

# Read and parse the input
f = open('input.txt', 'r')
sequence = f.read().split(',')

# Vars for the result
total_value = 0
boxes = dict()

# For every word in the sequence
for word in sequence:
    
    # Add the hash value to the total
    total_value += get_hash(word)
    
    # Perform the specified instruction
    if word[-1] == '-':
        remove_lens(boxes, word)
    else:
        add_lens(boxes, word)
        
    
print(f'The total hash value of the instructions is {total_value}')
print(f'The focus power after performing the instructions is {get_focus_power(boxes)}')