from itertools import combinations

# Class to represent a snailfish number
class Pair:
    
    # Constructer. Takes a depth, a string representation and a parent as parameters
    def __init__(self, depth = 0, number = '', parent = None):
        
        # Set some default values
        self.depth = depth
        self.left = None
        self.right = None
        self.value = -1
        self.parent = parent
        
        # If number is empty, do nothing
        if len(number) == 0:
            return
        
        # If number is a single digit, set the value and do nothing else
        if len(number) == 1:
            self.value = int(number)
            return
        
        # Locate left and right part of the pair
        bracket = -1
        split = -1
        for i, c in enumerate(number):
            
            if c == '[':
                bracket += 1
            elif c == ']':
                bracket -= 1
            elif c == ',' and bracket == 0:
                split = i
                break
        
        # Recursively create the left and right snailfish number
        self.left = Pair(depth + 1, number[1:split], self)
        self.right = Pair(depth + 1, number[split+1:-1], self)
    
    # Function to add two snailfish numbers
    def add(self, right):
        
        # Create a new pair
        new_pair = Pair(depth = -1)
        
        # Set the left snailfish number
        new_pair.left = self
        new_pair.left.parent = new_pair
        
        # Set the right snailfish number
        new_pair.right = right
        new_pair.right.parent = new_pair
        
        # Update all depths
        new_pair.update()  
        
        # Perform explosions
        new_pair.reduce()
        
        # Try to do splits. If a split is done, do explosions. Continue until no splits are done
        while new_pair.split():
            new_pair.reduce()
        
        # Return the new pair
        return new_pair
    
    # Function to update all depths
    def update(self):
        self.depth += 1
        
        if self.left:
            self.left.update()
        
        if self.right:
            self.right.update()

    # Function to explode a pair
    def explode(self):    
        
        # Find next left node
        cur = self
        
        # Go up until parent is to the right
        while cur.parent.left == cur:
            cur = cur.parent
            
            if not cur.parent:
                cur = None
                break
            
        # If we have found a parent to the right, we can add the number to something
        if cur and cur.parent:
        
            cur = cur.parent
            
            # Go left once, then go right until we are at a leaf
            next_left = cur.left
            while next_left.value == -1:
            
                if not next_left.right:
                    break
            
                next_left = next_left.right
            
            # Add number to the found leaf
            if not next_left.value == -1:
                next_left.value += self.left.value
        
        # Find next right node
        cur = self
        
        # Go up until parent is to the left
        while cur.parent.right == cur:
            cur = cur.parent
        
            if not cur.parent:
                cur = None
                break
        
        # If we have found a parent to the left, we can add the number to something
        if cur and cur.parent:
        
            cur = cur.parent
            
            # Go right once, then go left until we are at a leaf
            next_right = cur.right
            while next_right.value == -1:
            
                if not next_right.left:
                    break
            
                next_right = next_right.left
        
            # Add number to the find leaf
            if not next_right.value == -1:
                next_right.value += self.right.value
        
        # Set the value to zero and delete the children
        self.value = 0
        self.left = None
        self.right = None
    
    # Function to split a number
    def split(self):
        
        # Assume that we do not need to split anything
        updated = False
        
        # First recurse all the way to the left
        if self.left:
            updated = self.left.split() or updated
            
            
        # If we need to split
        if self.value and self.value > 9:
            
            # Calculate the values we need
            v_left = int(self.value/2)
            if self.value % 2 == 0:
                v_right = int(self.value/2)
            else:
                v_right = int(self.value/2) + 1
                
            # Set the values for the new
            self.value = -1
            self.left = Pair()
            self.left.value = v_left
            self.left.parent = self
            self.left.depth = self.depth + 1
            self.right = Pair()
            self.right.value = v_right
            self.right.parent = self
            self.right.depth = self.depth + 1
            
            # Return, so we stop splitting                                  
            return True
            
        # If we have updated anything, stop recursing
        if updated:
            return True
        
        # Finally recurse right
        if self.right:
            updated = self.right.split() or updated

        # Return whether or nor we have updated the node
        return updated

    # Function to help explode the numbers
    def reduce(self):
        
        # Function to know whether we have explodet anything
        updated = False
        
        # First recurse all the way to the left
        if self.left:
            updated = self.left.reduce() or updated

        # If we need to explode a pair, do so. Then start at the root again
        if self.depth == 4 and self.value == -1 and self.left and self.right:
            self.explode()
            
            root = self
            
            while root.parent:
                root = root.parent
                
            root.reduce()
            
        # Then recurse to the right
        if self.right:
            updated = self.right.reduce() or updated
            
        # Return whether or not we have updated anything
        return updated
            
    # Function to get the magniture
    def get_magnitude(self):
        
        if not self.value == -1:
            return self.value
        
        return (3 * self.left.get_magnitude()) + (2 * self.right.get_magnitude())
        
# Open input and read as lines
f = open('input.txt', 'r')
lines = f.read().split('\n')

# Init the first number
pair = Pair(number = lines[0])

# Add each other number
for l in lines[1:]:
    pair = pair.add(Pair(number = l))
    
# Find the maximum magnitude after pairwise adding of the numbers
max_magnitude = -1
for c in list(combinations(lines, 2)):
    magnitude = Pair(number = c[0]).add(Pair(number = c[1])).get_magnitude()
    
    if magnitude > max_magnitude:
        max_magnitude = magnitude
    
    magnitude = Pair(number = c[0]).add(Pair(number = c[1])).get_magnitude()

    if magnitude > max_magnitude:
        max_magnitude = magnitude

# Print the results
print('The magnitude of the final result is ' + str(pair.get_magnitude()))
print('The maximum magnitude after pairwise addition is ' + str(max_magnitude))