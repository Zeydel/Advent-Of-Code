# Parse the workflow into a dict of lists of functions
def parse_workflows(workflows):
    
    # Split by line
    workflows = workflows.split('\n')
    
    # Dict for the parsed workflows
    parsed_workflows = {}
    
    # For every line
    for w in workflows:
        
        # Create an empty list
        workflow = []
        
        # Split the data
        name, flow = w.split('{')
        flow = flow[:-1].split(',')
        
        # For every flow until the last
        for f in flow[:-1]:
            
            # Extract the values
            val = f[0]
            sign = f[1]
            limit, result = f.split(sign)[1].split(':')
            limit = int(limit)
            
            # If the sign is >, create a greater than function with the specifed paramters
            if sign == '>':
                def grt(e, val=val, limit=limit, result=result):
                    if e[val] > limit:
                        return result
                    return ''
                
                workflow.append(grt)
                
            # Else, create a less than function with the specified parameters
            else:                
                def lss(e, val=val, limit=limit, result=result):
                    if e[val] < limit:
                        return result
                    return ''
                workflow.append(lss)
        
        # Create a function returning a value for the last part of the workflow
        def rtn(e, result=flow[-1]):
            return result
        
        workflow.append(rtn)
        
        # Add to the dict
        parsed_workflows[name] = workflow
    
    # Return the dictionary
    return parsed_workflows

# Function to parse the parts into dicts
def parse_parts(parts):
    
    # Split by line
    parts = parts.split('\n')
    parsed_parts = []
    
    # For every line
    for p in parts:
        
        part = dict()
        
        # Extract the values, and add to a dict
        p = p[1:-1].split(',')
        
        for spec in p:
            
            name, val = spec.split('=')
            part[name] = int(val)
            
        parsed_parts.append(part)
        
    return parsed_parts
    
# Get the sum of parts
def get_part_sum(parts):
    
    part_sum = 0
    
    # For every key in every part, add the value
    for p in parts:
        
        for k in p:
            part_sum += p[k]
            
    return part_sum

# Preprocess workflows before calculating the number of combinations
def preprocess_workflows(workflows):
    
    workflows = workflows.split('\n')
    
    parsed_workflows = {}
    
    # For every workflow
    for w in workflows:
        workflow = []
        
        # Get the name and the values
        name, flow = w.split('{')
        flow = flow[:-1].split(',')
        
        for f in flow[:-1]:
            
            val = f[0]
            sign = f[1]
            limit, result = f.split(sign)[1].split(':')
            limit = int(limit)
            
            # Add a tuple with the parameters
            workflow.append((val, sign, limit, result))
            
        # Add the final part as a simple value
        workflow.append(flow[-1])
        
        # Add the parsed workflow
        parsed_workflows[name] = workflow
        
    return parsed_workflows

# Get the number of combinations
def get_combinations_count(workflows, flow, ranges):
    
    # Initially zero
    combinations = 0
    
    # If part is rejected, return 0
    if flow == 'R':
        return combinations
    
    # If part is accepted
    elif flow == 'A':
        combinations = 1
        
        # Multiple the length of all ranges
        for k in ranges:
            
            combinations *= (ranges[k][1]+1) - ranges[k][0] 
    
        # Return the result
        return combinations
    
    # Get the specifed workflow
    workflow = workflows[flow]
    
    # Copy the dictionary
    range_copy = {k: ranges[k] for k in ranges}
    
    # For every tuple until the last
    for val, sign, limit, result in workflow[:-1]:
        
        # If the sign is less than
        if sign == '<':
            
            # Create a copy of the ranges
            range_less = {k: range_copy[k] for k in range_copy}
            
            # Edit the range of the specified value to be less than the limit
            range_less[val] = (range_less[val][0], limit-1)
            
            # Edit the range in the copy of the dict to equal to or more than the limit
            range_copy[val] = (limit, range_copy[val][1])
            
            # Recurse with the new range
            combinations += get_combinations_count(workflows, result, range_less)
        
        # Does the same as above, but with greater than
        else:
            range_more = {k: range_copy[k] for k in range_copy}
            range_more[val] = (limit+1, range_more[val][1])
            range_copy[val] = (range_copy[val][0], limit)
            
            combinations += get_combinations_count(workflows, result, range_more)
            
    # Add the number of combinations for the default case
    combinations += get_combinations_count(workflows, workflow[-1], range_copy)
    
    # Return the count
    return combinations
            
    

# Read and parse the input
f = open('input.txt', 'r')
workflows, parts = f.read().split('\n\n')

# Parse the input
workflows_functions = parse_workflows(workflows)
parts = parse_parts(parts)

# List of accepted parts
accepted_parts = []

# For every part
for p in parts:
    
    # Run it through the workflows until either accepted or rejected
    flow = 'in'
    while flow not in ('A', 'R'):
        
        workflow = workflows_functions[flow]
        
        for f in workflow:
            result = f(p)
            if result:
                flow = result
                break
                
    # If it is accepted, add it to list of accepted parts
    if flow == 'A':
        accepted_parts.append(p)
        
# Init list of ranges   
init_ranges = {'x': (1,4000),
               'm': (1,4000),
               'a': (1,4000),
               's': (1,4000)}

# Preprocess the workflows
parsed_workflows = preprocess_workflows(workflows)
        
# Calculate the results
accepted_parts_sum = get_part_sum(accepted_parts)
combination_parts = get_combinations_count(parsed_workflows, 'in', init_ranges)

# Print the results
print(f'The sum of the accepted parts is {get_part_sum(accepted_parts)}')
print(f'The number of accepted combinations is {combination_parts}')