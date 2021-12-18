# Class to represent a node in a tree
class Node:
    
    # Constructer. Takes a binary string and constructs subtree
    def __init__(self, binary_string):
        
        # Read the version from the string as int and remove it from the string
        self.version = int(binary_string[:3],2)
        binary_string = binary_string[3:]
        
        # Read the id from the string as int and remove it
        self.id = int(binary_string[:3],2)
        binary_string = binary_string[3:]
        
        # Init var for the binary length of the string
        self.binary_length = 6
        
        # Init empty list of children
        self.children = []
        
        # If id is 4, the node has a simple value
        if self.id == 4:
            
            # Construct the binary value
            binary_number = ''
            while True:
                
                # If we see a zero, we are at the last byte
                last_bit = binary_string[0] == '0'
                binary_string = binary_string[1:]
                
                # Read the next four bits into the string
                binary_number += binary_string[:4]
                binary_string = binary_string[4:]
                
                # Increase the binary length counter
                self.binary_length += 5
                
                # Exit the loop if we are at the last bit
                if last_bit:
                    break
            
            # Assign the value of the binary string
            self.value = int(binary_number, 2)
        
        # If length type is zero
        elif binary_string[0] == '0':
            binary_string = binary_string[1:]
            
            # Read the expected length of the sub-packets
            length = int(binary_string[:15], 2)
            binary_string = binary_string[15:]
            
            # Create counter for total length
            total_length = 0
            
            # While we are not at the total length
            while True:
                
                # Crate the child node
                child = Node(binary_string)
                
                # Remove the child node from the string
                binary_string = binary_string[child.binary_length:]
                
                # Add child to list of children
                self.children.append(child)
                
                # Add to total length
                total_length += child.binary_length
                
                # If we are at the total length, exit loop
                if total_length == length:
                    break
                
            # Set the binary length of the node
            self.binary_length += total_length + 16
            
        # Else, length type is one
        else:
            binary_string = binary_string[1:]
            
            # Read the expected count of sub-packets
            count = int(binary_string[:11], 2)
            binary_string = binary_string[11:]
            
            # Init var for total length
            total_length = 0
            
            # Do i times
            for i in range(count):
                
                # Crate the child node
                child = Node(binary_string)

                # Remove the child node from the string
                binary_string = binary_string[child.binary_length:]

                # Add child to list of children
                self.children.append(child)
                
                # Add to total length
                total_length += child.binary_length
                
            # Set the binary length of the node
            self.binary_length += total_length + 12
       
    # Function to sum the version numbers using inorder traversal
    def sum_version_numbers(self):
        
        # Add own version number
        version_number_sum = self.version
        
        # Add each childs version number
        for c in self.children:
            version_number_sum += c.sum_version_numbers()
            
        # Return sum
        return version_number_sum
            
    # Function to get value of a node
    def get_value(self):
        
        # Start value at zero
        value = 0
        
        # If id is zero, sum the childrens values
        if self.id == 0:
            
            for c in self.children:
                value += c.get_value()
                    
        # If id is 1, take the product of the childrens values
        elif self.id == 1:
            
            value = 1
            
            for c in self.children:
                value *= c.get_value()
                
        # If id is 2, take the minimum of the childrens values
        elif self.id == 2:
            
            values = []
            
            for c in self.children:
                values.append(c.get_value())
                
            value = min(values)
            
        # If id is 3, take the maximum of the childrens values
        elif self.id == 3:
        
            values = []
            
            for c in self.children:
                values.append(c.get_value())
                
            value = max(values)
                
        # If id is 4, take the value of the node
        elif self.id == 4:
            
            value = self.value
            
        # If id is 5, take 1 if first child has higher value than second child. Else take 0
        elif self.id == 5:
            
            if self.children[0].get_value() > self.children[1].get_value():
                value = 1
            else:
                value = 0
                
        # If id is 5, take 0 if first child has higher value than second child. Else take 1
        elif self.id == 6:
         
            if self.children[0].get_value() < self.children[1].get_value():
                value = 1
            else:
                value = 0
                
        # If id is 5, take 1 if first child has equal value to second child. Else take 0
        elif self.id == 7:
         
            if self.children[0].get_value() == self.children[1].get_value():
                value = 1
            else:
                value = 0
            
        # Return the value
        return value

# Open file and read as one string
f = open('input.txt', 'r')
hex_string = f.read()

# Convert string to binary
binary_string = bin(int(hex_string, 16))[2:]

# Construct tree
node = Node(binary_string)

# Print the results
print('The sum of all version numbers in the packets is ' + str(node.sum_version_numbers()))
print('The value of the root node is ' + str(node.get_value()))