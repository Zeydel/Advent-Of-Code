# Parse the input into rules and books
def parse(lines):
    
    rules = []
    
    split_idx = -1
    
    for i, line in enumerate(lines):
        
        if line == '':
            split_idx = i
            break
        
        split_line = line.split('|')
        
        rules.append((int(split_line[0]), int(split_line[1])))
        
    lines = lines[split_idx+1:]
    
    pages = []
    
    for line in lines:
        
        split_line = line.split(',')
        
        pages.append([int(num) for num in split_line])
        
    return rules, pages

# Check wether a book is correctly ordered
def book_is_correct(rules, page):
    
    # For every rule
    for rule1, rule2 in rules:
        
        # We only care about rules where both numbers appear
        # in the list
        if rule1 not in page or rule2 not in page:
            continue
        
        # If the index of the first number is greater
        # than the index of the second number, return false
        if page.index(rule1) > page.index(rule2):
            return False
    
    # If we haven't broken any rules, return true
    return True
            
# Give a page and the set of rules, return the set of
# prerequsites for numbers in the page
def build_prereq_list(rules, page):
    
    # Init empty dict
    prereqs = dict()
    
    # For every pair of rules
    for rule1, rule2 in rules:
        
        # We only pair about rules where bouth numbers appear on the page
        if rule1 not in page or rule2 not in page:
            continue
        
        # Add both rules to the dict
        if rule1 not in prereqs:
            prereqs[rule1] = []
            
        if rule2 not in prereqs:
            prereqs[rule2] = []
            
        # Add the first number as a prerequiste for the second
        prereqs[rule2].append(rule1)
        
    return prereqs

# Correct an incorrectly ordered book
def correct_book(rules, page):
    
    # Find the list of prereqs
    prereqs = build_prereq_list(rules, page)
    
    # Init var to store the fixed book
    corrected = []
    
    i = 0
    
    
    # We first find the book with 0 prereqs, then the one with 1 and so on
    # This assumes that there exists one unique solutions for each book
    while i < len(page):
        
        for rule in prereqs:
            
            if len(prereqs[rule]) == i:
                corrected.append(rule)
                break
            
        i += 1
        
    return corrected
        
# Open file and read lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
rules, pages = parse(lines)

# Init vars for results
middle_sum = 0
middle_sum_corrected = 0

# For every page
for page in pages:
    
    # If it is already correct, add to result
    if book_is_correct(rules, page):
        middle_sum += page[len(page)//2]
        
    # Otherwise correct book and add to other results
    else:
        corrected = correct_book(rules, page)
        middle_sum_corrected += corrected[len(corrected)//2]
        
# Print the results
print(f'{middle_sum} is the sum of middle numbers of correct books')
print(f'{middle_sum_corrected} is the sum of middle numbers of corrected books')