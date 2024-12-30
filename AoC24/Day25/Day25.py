# Parse input into keys and locks
def parse(blocks):
    
    keys = []
    locks = []
    
    for block in blocks:
        
        lines = block.split()
        heights = [-1] *len(lines[0])
        
        height = len(lines) - 2
        
        for h in range(len(lines)):
            
            for w in range(len(lines[0])):
                
                heights[w] += 1 if lines[h][w] == '#' else 0
                
        if lines[0][0] == '.':
            keys.append(heights)
        else:
            locks.append(heights)
            
    return keys, locks, height
                
# Determe if a key fits a lock
def key_fits(key, lock, height):
    
    for i, k in enumerate(key):
        
        if k + lock[i] > height:
            return False
        
    return True

# Get number of keys that fit
def get_fits(keys, locks, height):
    
    fits = 0
    
    for key in keys:
        for lock in locks:
            if key_fits(key, lock, height):
                fits += 1
                
    return fits

# Open file and read as blocks of lines
file = open('input.txt', 'r')
blocks = [line.strip() for line in file.read().split('\n\n')]

# Get keys, locks and lock heights
keys, locks, height = parse(blocks)

# Get number of keys that fit
fits = get_fits(keys, locks, height)

# Print the results
print(f'{fits} is the number of keys that fit')