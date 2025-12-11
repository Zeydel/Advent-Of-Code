# Parse the input into a dictionary of cables and where they go
def parse(lines):
    
    cables = dict()
    
    for line in lines:
        
        key, values = line.split(': ')
        
        cables[key] = values.split()
        
    return cables

# Recursive function with memoization to get the number of paths from start to end
def get_lines(start, end, cables, memo_dict=dict()):
    
    if start in memo_dict:
        return memo_dict[start]
    
    if start == end:
        memo_dict[start] = 1
        return memo_dict[start]
    
    lines = 0
    
    for cable in cables[start]:
        
        lines += get_lines(cable, end, cables, memo_dict)
        
    memo_dict[start] = lines
    return memo_dict[start]

# Same as above, but add missing dangerous cables to state
def get_lines_containing_cables(start, end, cables, dangerous_cables, memo_dict=dict()):
    
    dict_key = (start, tuple(dangerous_cables))
    
    if dict_key in memo_dict:
        return memo_dict[dict_key]
    
    if start == end and len(dangerous_cables) == 0:
        memo_dict[dict_key] = 1
        return memo_dict[dict_key]
    elif start == end:
        memo_dict[dict_key] = 0
        return memo_dict[dict_key]
    
    lines = 0
    
    for cable in cables[start]:
        
        lines += get_lines_containing_cables(cable, end, cables, dangerous_cables - {cable}, memo_dict)
        
    memo_dict[dict_key] = lines
    return memo_dict[dict_key]


# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse input
cables = parse(lines)

# Define start and end values
you_start = 'you'
server_start = 'svr'

end = 'out'

dangerous_cables = {'dac', 'fft'}

# Get lines from you to out
lines = get_lines(you_start, end, cables)

# Get lines from svt to out containing dangerous cables
lines_with_dangerous_cables = get_lines_containing_cables(server_start, end, cables, dangerous_cables)

print(f'There are {lines} from {you_start} to {end}')
print(f'There are {lines_with_dangerous_cables} from {server_start} to {end} containging the dangerous cables')