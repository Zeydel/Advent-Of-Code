# Parse the input string into a list of numbers
def parse(input_string):
    
    return [int(num) for num in input_string]

# Parse the input string into list of tuples containg file id and block length
def parse_continous(input_string):
    
    blocks = []
    block_id = 0
    
    for i, c in enumerate(input_string):
        
        if i % 2 == 0:
            blocks.append((int(c), block_id))
            block_id += 1
        else:
            blocks.append((int(c), -1))
            
    return blocks
        
        
    
# Given a block width, starting block id and file id, get the checksum
def get_block_checksum(num, start_block_id, file_id):
    
    checksum = 0
    
    for i in range(num):
        checksum += file_id * start_block_id
        start_block_id += 1
    
    return checksum

# Get checksum for memory without actually moving the memory arounjd
def get_checksum(memory):
            
    # Init head and tail index
    head_idx = 0
    tail_idx = len(memory) - 1
    
    # Init block id and checksum
    block_id = 0
    
    checksum = 0
    
    # We area taking the input from both ends. Stop when we meet in the middle
    while head_idx <= tail_idx:
        
        # Get the num at each index
        head_num = memory[head_idx]
        tail_num = memory[tail_idx]
        
        # Get the id of the block at the head and the tail
        head_id = head_idx // 2
        tail_id = tail_idx // 2
        
        # If we are at an odd index in the head, we are at a place that wont move
        # get the checksum contribution of that block
        if head_idx % 2 == 0:
            block_checksum = get_block_checksum(head_num, block_id, head_id)
            memory[head_idx] = 0
            
            head_idx += 1
            
            block_id += head_num
            
        # If we are at an odd index, at the head, figure out if we can place the number
        # at the tail index in its place. Get the checksum contribution of the
        # moved block in that place
        elif head_num > tail_num:
            block_checksum = get_block_checksum(tail_num, block_id, tail_id)
            memory[head_idx] -= tail_num
            
            block_id += tail_num
            tail_idx -= 2
        elif head_num <= tail_num:
            block_checksum = get_block_checksum(head_num, block_id, tail_id)
            memory[tail_idx] -= head_num
            
            block_id += head_num
            head_idx += 1
            
        checksum += block_checksum
            
    return checksum
    
  
# Get the checksum of the continous memory blocks
def get_checksum_continous(memory):
    
    # Init tail index
    tail_idx = len(memory) - 1
    
    # While we are still within range
    while tail_idx >= 0:
        
        # Get the size and id of current block
        block_size, block_id = memory[tail_idx]
        
        # If we are at an empty spot, continue
        if block_id == -1:
            tail_idx -= 1
            continue
        
        # Find a place to place the current block, starting from left
        for i in range(tail_idx):
            
            i_size, i_id = memory[i]
            
            # If we can place the block here
            if i_size >= block_size and i_id == -1:
                
                # Replace the block that we just moved
                memory = memory[:tail_idx] + [(block_size, -1)] + memory[tail_idx+1:]
                
                # Add the moved block and remainder of the empty block in place
                memory = memory[:i] + [(block_size, block_id), (i_size - block_size, -1)] + memory[i+1:]
                
                # Incement because we have just added an element to the middle of the list
                tail_idx += 1
                break
            
        tail_idx -= 1
        
    # Init checksum and block id
    checksum = 0
    start_block_id = 0
    
    # For every block in memoeryh
    for block_size, block_id in memory:
        
        # If we are not at an empty block, add its contribution to the checksum
        if block_id != -1:
            checksum += get_block_checksum(block_size, start_block_id, block_id)
        
        # Add the block size to the start block id
        start_block_id += block_size
            
    return checksum
                
# Open file and read as string
file = open('input.txt', 'r')
input_string = file.readline()

# Parse input for each of the problems
memory = parse(input_string)

memory_continous = parse_continous(input_string)

# Get both checksums
checksum = get_checksum(memory)

checksum_continous = get_checksum_continous(memory_continous)

# Print the results
print(f'{checksum} is the checksum when moving files individually')
print(f'{checksum_continous} is the checksum when moving files in blocks')
