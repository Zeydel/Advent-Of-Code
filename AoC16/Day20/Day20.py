# Parse the input into a list of tuples
def parse(banlist):
    bannedIps = []
    for b in banlist:
        split = b.split('-')
        bannedIps.append((int(split[0]), int(split[1])))
        
    return bannedIps

# Function to get the set of Ips that are not banned
def getUnbannedIps(bannedIps):
    
    # Init empty set
    UnbannedIps = set()
    
    # Start from 0 and go to the maximum integer allowed
    i = 0
    while i <= 4294967295:
        
        # Assume that the ip is allowed
        collision = ()
        
        # For every banned Ip
        for b in bannedIps:
            
            # If we hit an it, save it and break
            if b[0] <= i and i <= b[1]:
               collision = b
               break
         
        # If we have hit something, jump past the max in that range
        if collision != ():
            i = b[1]+1
        # Else increment and add the ip to the set
        else:
            i += 1
            UnbannedIps.add(i)
        
    # Return the set
    return UnbannedIps

# Read and parse the input
f = open('input.txt', 'r')
banlist = f.read().split('\n')
bannedIps = parse(banlist)

# Get the set of unbanned Ips
UnbannedIps = getUnbannedIps(bannedIps)

# Print the results
print(f'The minimum unbanned Ip is {min(UnbannedIps)}')
print(f'In total, there are {len(UnbannedIps)} unbanned Ips')
