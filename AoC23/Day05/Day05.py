# Class representing the maps found in the almanac
class AlmanacMap:
    
    # Init with empty lists
    def __init__(self):
        self.destinations = []
        self.sources = []
        self.ranges = []
        
    # Function to map a number in the list
    def mapNumber(self, number):
        
        # Init source and destination variables
        src = -1
        des = -1
        
        # Look for a range where the number fits
        for i, s in enumerate(self.sources):
            if s <= number and s + self.ranges[i] > number:
                src = s
                des = self.destinations[i]
                break
            
        # If we didn't find any, return the number
        if src == -1:
            return number
        
        # Otherwise return the destination number, plus the offset from the source
        return des + (number - src)
    
    
    # Perform the same mapping as above, just in reverse
    def mapReverse(self, number):
        
        des = -1
        src = -1
        
        for i, d in enumerate(self.destinations):
            if d <= number and d + self.ranges[i] > number:
                des = d
                src = self.sources[i]
                break
            
        if des == -1:
            return number
        
        return src + (number - des)
                

# Read and parse the input
f = open('input.txt', 'r')
almanac = f.read().split('\n\n')

# Get the seeds
seeds = [int(seed) for seed in almanac[0].split(': ')[1].split()]

# Get the seeds, but with the range representation
seedRanges = []

for i, s in list(enumerate(seeds))[::2]:    
    seedRanges.append((s, seeds[i+1]))
    
# Construct the maps
maps = []
for page in almanac[1:]:
    
    almanacMap = AlmanacMap()
    for line in page.split('\n')[1:]:
        des, src, rng = [int(val) for val in line.split()]
        
        almanacMap.destinations.append(des)
        almanacMap.sources.append(src)
        almanacMap.ranges.append(rng)
        
    maps.append(almanacMap)
    
# Vars for the result
lowestLocation = float('inf')
lowestLocationRange = -1

# For every seed
for seed in seeds:
    
    # Run it through every map
    for m in maps:
        seed = m.mapNumber(seed)
        
    # If we have a new lowest location, save it
    if seed < lowestLocation:
        lowestLocation = seed
      
# Start searching for lowest location at 0
location = 0

# While we havent found a seed
while lowestLocationRange == -1:
    
    # Run the location through every map in reverse order
    seed = location
    for m in maps[::-1]:
        seed = m.mapReverse(seed)
        
    # Check if the found seed number belong in any range
    for seedRange in seedRanges:
        
        # If it does, save it. Then exit loop
        if seedRange[0] <= seed and seed < seedRange[0] + seedRange[1]:
            lowestLocationRange = location
    
    location += 1
    
# Print the results
print(f'The lowest seed location given the initial list of seeds is {lowestLocation}')
print(f'The lowest seed location given the seed ranges is {lowestLocationRange}')        
