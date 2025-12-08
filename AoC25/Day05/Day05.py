# Parse the input into a listof ranges and a list of ids
def parse(lines):
    
    ranges = lines[:lines.index('')]
    
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]
    
    ids = lines[lines.index('')+1:]
    
    ids = [int(i) for i in ids]
    
    return ranges, ids

# Given an id, check wether it is fresh by checking if it is contained in any raneges
def is_fresh(food_id, food_ranges):
    
    for start, end in food_ranges:
        
        if food_id >= start and food_id <= end:
            return True
        
    return False

# For every id, check if it contained in any ranges
def get_fresh_ingredient_count(ranges, ids):
    
    fresh_ingredients = 0
    
    for food_id in ids:
        
        if is_fresh(food_id, ranges):
            fresh_ingredients += 1
        
    return fresh_ingredients

# Given the ranges, join the ones that overlap
def join_ranges(ranges):
    
    # Loop variable
    ranges_joined = True
    
    # Init a set of new ranges
    new_ranges = set(ranges)
    
    # While we have joined ranges in an iteration
    while ranges_joined:
        
        # Assume that we are unable to join ranges
        ranges_joined = False
        
        # For every pair of ranges
        for r1_start, r1_end in ranges:
            for r2_start, r2_end in ranges:
                
                # If it is the same range, continue
                if r1_start == r2_start and r1_end == r2_end:
                    continue
                
                # If one range is contained within the other, remove that range
                if r1_start >= r2_start and r1_end <= r2_end and (r1_start, r1_end) in new_ranges:
                    
                    new_ranges.remove((r1_start, r1_end))
                
                    ranges_joined = True
                
                # If one range overlaps with another, add a new, bigger range
                elif r2_start > r1_start and r2_start <= r1_end:
                                        
                    new_ranges.add((r1_start, r2_end))
                    
                    ranges_joined = True
                    
        # Update the ranges
        ranges = {r for r in new_ranges}
                    
    # Return the new ranges
    return new_ranges

# Given the ranges, return the number of ids
def get_id_count(ranges):
    
    count = 0
    
    for r in ranges:
        
        count += (r[1] - r[0]) + 1
        
    return count

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
ranges, ids = parse(lines)

# Count the fresh ingredients
fresh_ingredient_count = get_fresh_ingredient_count(ranges, ids)

# Join all ranges
joined_ranges = join_ranges(ranges)

# Get the total id count
id_count = get_id_count(joined_ranges)

# Print the results
print(f'{fresh_ingredient_count} ingredients are fresh')
print(f'{id_count} ingredient ids are fresh according to the ranges')