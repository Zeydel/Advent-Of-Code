# Parse the input into a list for each column
def parse(lines):
    
    left_list = []
    right_list = []
    
    # For every line, split 
    for line in lines:
        left_num, right_num = line.split()
        
        # Add number to each list after converting to int
        left_list.append(int(left_num))
        right_list.append(int(right_num))
        
    # Sort the list
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    
    # Retun both lists
    return left_list, right_list

# Get the sum of differences
def get_difference_sum(left_list, right_list):
    
    # Init as zero
    difference_sum = 0
    
    # For every index of the lists
    for i in range(len(left_list)):
        
        # Add the absolute value of the differnce to the sum
        difference_sum += abs(left_list[i] - right_list[i])
        
    # Return the sum
    return difference_sum

# Get the similarity score
def get_similarity_score(left_list, right_list):
    
    # Init as zero
    similarity_score = 0
    
    # For every number in left list
    for left in left_list:
        
        # Count number of occurrences in the right list
        occurrences = 0
        for right in right_list:
            
            if right == left:
                occurrences += 1
                
        # Add the result to the similarity score
        similarity_score += left * occurrences
        
    # Return the result
    return similarity_score
        
# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
left_list, right_list = parse(lines)

# Compute the results

difference_sum = get_difference_sum(left_list, right_list)
similarity_score = get_similarity_score(left_list, right_list)

print(f'{difference_sum} is the sum of differences')
print(f'{similarity_score} is the similarity score')