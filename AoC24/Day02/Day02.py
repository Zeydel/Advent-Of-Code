# Parse the input
def parse(lines):
    
    reports = []
    
    # Parse each line as a list of numbers
    for line in lines:
        reports.append([int(num) for num in line.split()])

    return reports

# Find out if report is safe
def is_safe(report):
    
    # Assume sequence is increasing
    increasing = True
    
    # If the sart of the sequence is decreasing, the whole sequence must be
    if report[0] > report[1]:
        increasing = False
        
    # For every pair of sequental numbers
    for i in range(len(report) - 1):
        
        # It sequence is supposed increase but it decreases, return false
        if increasing and report[i] > report[i+1]:
            return False
        # If sequence is supposed to decrease but in increases, return false
        elif not increasing and report[i] < report[i+1]:
            return False
        
        # If the difference is more than three or zero, return false
        if abs(report[i] - report[i+1]) > 3 or report[i] == report[i+1]:
            return False
        
    # Otherwise return true
    return True
    
# Find out if repot can be made safe by removed a single number
def can_be_safe(report):
    
    # If report is already safe, return true
    if is_safe(report):
        return True
    
    # Otherwise check for each number, if removing it makes the report safe
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
        
    # If nothing can make the report safe, retur nfalse
    return False

# Open file and read as lines
file = open('input.txt', 'r')
lines = [line.strip() for line in file.readlines()]

# Parse the input
reports = parse(lines)

# Init result counts
safe_reports = 0
potentially_safe_reports = 0

# For each report
for report in reports:
    
    # Increment counter if report is safe
    if is_safe(report):
        safe_reports += 1

    # Increment counter if report can be made safe
    if can_be_safe(report):
        potentially_safe_reports += 1
        
        
# Print the results
print(f'{safe_reports} reports are safe')
print(f'{potentially_safe_reports} can be made safe by removing one number')