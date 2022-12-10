# Open input and read as strings
f = open('input.txt', 'r')
signal = f.read()

# Init the result vars
firstUnique = -1
firstUniqueLong = -1

# Find the first substring with unique characters of length 4
for i in range(4, len(signal)):
    
    if len(signal[i-4:i]) == len(set(signal[i-4:i])):
        firstUnique = i
        break
    
# Find the first substring with unique characters of length 14
for i in range(14, len(signal)):

    if len(signal[i-14:i]) == len(set(signal[i-14:i])):
        firstUniqueLong = i
        break
        
    
# Print the results
print(f'The first substring with unique letters comes after {firstUnique} letters')
print(f'The first substring with unique letters comes after firstUniqueLong letters')