# Class for a tree node
class Node:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []

# Parse the input into a tree
def parse(output):
    
    # Define the root
    root = Node("root")
    
    # Set the current node
    cur = root
    
    # For every output line
    for o in output:
        
        # Split to parse
        l = o.split(" ")
        
        if len(l) == 2:
            
            # Add a file
            if l[0].isnumeric():
                cur.children.append(Node(l[1], cur, int(l[0])))
            
            # Add a dir
            elif l[0] != "$":
                cur.children.append(Node(l[1], cur))
        
        else:
            
            # Go to root
            if l[1] == "cd" and l[2] == "/":
                cur = root
                
            # Go to parent
            elif l[1] == "cd" and l[2] == "..":
                cur = cur.parent
                
            # Go to given children
            else:
                for c in cur.children:
                    if c.name == l[2]:
                        cur = c
                        break
                    
    # Return to root
    return root

# Traverse the tree and set sizes to all dirs
def setSize(root):
    
    # Start on zero
    mysum = 0
    
    # Add all folders and files
    for c in root.children:
        if c.size == 0:
            mysum += setSize(c)
        else:
            mysum += c.size
    
    # Set own size
    root.size = mysum

    return mysum
            
# Get the sum of the sizes of the small dirs  
def getSmallDirSum(node):
    
    # Init as zero
    smallSum = 0
    
    # Add all the small children
    for c in node.children:
        if c.children:
            smallSum += getSmallDirSum(c)

    # If current node is small add to current sum else return the sum
    if node.size <= 100000:
        return smallSum + node.size
    else:
        return smallSum
    
# Get the smallest folder over a given size
def getSmallestBigFolder(node, toDelete, curbest = float('inf')):

    # If we are within the bouds, we are the new best
    if node.size >= toDelete and node.size < curbest:
        curbest = node.size
        
    # Check all children
    for c in node.children:
        curbest = getSmallestBigFolder(c, toDelete, curbest)
        
    # Return the current best
    return curbest

# Open input and read as strings
f = open('input.txt', 'r')
output = f.read().split('\n')

# Parse the lines and set the sizes
root = parse(output)
setSize(root)

# Calculate how much data we need to delete
totalDisk = 70000000
updateSize = 30000000
unused = totalDisk - root.size
toDelete = updateSize - unused

# Print the results
print(f'The sum of small dirs is {getSmallDirSum(root)}')
print(f'The smallest folder we can delete is {getSmallestBigFolder(root, toDelete)}')