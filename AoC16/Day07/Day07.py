# Need regex package to find substrings
import regex as re

# Parse an address into the Hypernet Sequence and the remaining text
def parse(address):
    
    # Pattern to find Hypernet Sequences
    pattern = r'\[[a-z]+\]'
    hypernetSequences = re.findall(pattern, address)
    # Remove the brackets
    hypernetSequences = [hs.strip('[]') for hs in hypernetSequences]
    # Split the text on the Hypernet Sequnces to obtain the remaining text
    text = re.split(pattern, address)
    return (text, hypernetSequences)

# Return true if the string has an ABBA
def hasAbba(texts):
    # Pattern to find an ABBA (excluding AAAA's)
    pattern = r'(.)(.)\2(?!\2)\1'
    # Return true if pattern is found anywhere
    return any([re.search(pattern, t) for t in texts])

# Gets all ABA patterns
def getAbas(texts):
    # Pattern to find ABA's excluding AAA's
    pattern = r'((.)(.)(?!\3)\2)'
    # Join the whole text together
    text = '@@'.join(texts)
    # Return all matches from the joined string
    return [m[0] for m in re.findall(pattern, text, overlapped=True)]

# Return true if the text has a BAB to match any of the ABA's
def hasBabs(texts, abas):
    # Construct the possible BAB's
    babs = [aba[1] + aba[0] + aba[1] for aba in abas]
    # Return true if any BAB is in any of the strings
    return any([any([bab in text for text in texts]) for bab in babs])

# Read input and split by lines
f = open('input.txt', 'r')
addresses = f.read().split('\n')

# Init counters
tlsCount = 0
slsCount = 0

# For each address
for a in addresses:
    
    # Parse it
    t, h = parse(a)
    
    # Check if it suppoerts tls
    if not hasAbba(h) and hasAbba(t):
        tlsCount += 1
        
    # Check if it supports sls
    abas = getAbas(t)
    if hasBabs(h, abas):
        slsCount += 1
        
# Print the result
print(f'{tlsCount} addresses support tls')
print(f'{slsCount} addresses support sls')