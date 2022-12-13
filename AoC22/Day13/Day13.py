# Function to check wether two packets are in order
def inOrder(left, right):
    
    # If they are both ints, evaluate as such
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        if left == right:
            return None
    
    # If they are both lists, compare list items
    if type(left) == list and type(right) == list:
        for i in zip(left, right):
            order = inOrder(i[0], i[1])
            
            if order in [True, False]:
                return order
            
        # If no list elements returned a value, check their lengths
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
        elif len(left) == len(right):
            return None
        
    # If one is a list and the other is an int, evaluate as such
    if type(left) == list and type(right) == int:
        return inOrder(left, [right])
    
    if type(left) == int and type(right) == list:
        return inOrder([left], right)
    
    
# Function to parse a string
def parse(string, idx = 1):
    
    # Create a list
    asList = []
        
    # While we are in bounds
    while idx < len(string):
        
        # If the index is a digit
        if string[idx].isdigit():
        
            # Find the full number
            number = string[idx]
            while string[idx+1].isdigit():
                number += string[idx]
                idx += 1
                
            # Add to the list
            asList.append(int(number))
            
        # If we have found the start of a list, recurse
        elif string[idx] == '[':
            sub, idx = parse(string, idx+1)
            asList.append(sub)
            
        # If we have found the end of a list, return
        elif string[idx] == ']':
            return (asList, idx)
        
        # Increment
        idx += 1
    
# Bubble sort packets
def sort(packets):
    
    # Just keep swapping
    for i in range(len(packets)):
        for j in range(len(packets)-(i+1)):
            if not inOrder(packets[j], packets[j+1]):
                packets[j], packets[j+1] = packets[j+1], packets[j]
                
    return packets


# Open input and read as strings
f = open('input.txt', 'r')
signal = f.read().split('\n')

# Index and index sum
idx = 1
indexSum = 0

# List of packets
packets = []

for i in list(range(len(signal)))[::3]:
    
    # Parse packets and add to list
    p1 = parse(signal[i])[0]
    p2 = parse(signal[i+1])[0]
    
    packets.append(p1)
    packets.append(p2)
    
    # Check if they are in order
    if inOrder(p1, p2):
        indexSum += idx
        
    idx += 1
        

# Add the divider packets
packets.append([[2]])
packets.append([[6]])

# Sort the packets
packets = sort(packets)

# Var for the dividerproduct
dividerProduct = 1

# Get the product of the indices of the divider packets
for i in range(len(packets)):
    if packets[i] == [[2]] or packets[i] == [[6]]:
        dividerProduct *= (i+1)
    
# Print the results
print(f'The sum of the indices of the packets in the right order is {indexSum}')
print(f'The product of the indices of the divider packets is {dividerProduct}')
# 5982 too high