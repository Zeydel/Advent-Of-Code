class Node:
    
    def __init__(self, binary_string):
        self.version = int(binary_string[:3],2)
        binary_string = binary_string[3:]
        
        self.id = int(binary_string[:3],2)
        binary_string = binary_string[3:]
        
        self.binary_length = 6
        
        self.children = []
        
        if self.id == 4:
            binary_number = ''
            
            
            while True:
                
                last_bit = binary_string[0] == '0'
                binary_string = binary_string[1:]
                
                binary_number += binary_string[:4]
                binary_string = binary_string[4:]
                
                self.binary_length += 5
                
                if last_bit:
                    break
            
            self.value = int(binary_number, 2)
        
        elif binary_string[0] == '0':
            binary_string = binary_string[1:]
            
            length = int(binary_string[:15], 2)
            binary_string = binary_string[15:]
            
            total_length = 0
            while True:
                child = Node(binary_string)
                binary_string = binary_string[child.binary_length:]
                self.children.append(child)
                total_length += child.binary_length
                
                if total_length == length:
                    break
                
            self.binary_length += total_length + 16
            
        else:
            binary_string = binary_string[1:]
            
            count = int(binary_string[:11], 2)
            binary_string = binary_string[11:]
            
            total_length = 0
            for i in range(count):
                child = Node(binary_string)
                binary_string = binary_string[child.binary_length:]
                self.children.append(child)
                total_length += child.binary_length
                
            self.binary_length += total_length + 12
         
    def sum_version_numbers(self):
        
        version_number_sum = self.version
        
        for c in self.children:
            version_number_sum += c.sum_version_numbers()
            
        return version_number_sum
            
    def get_value(self):
        
        value = 0

        
        if self.id == 0:
            
            for c in self.children:
                value += c.get_value()
                    
        elif self.id == 1:
            
            value = 1
            
            for c in self.children:
                value *= c.get_value()
                
        elif self.id == 2:
            
            values = []
            
            for c in self.children:
                values.append(c.get_value())
                
            value = min(values)
            
        elif self.id == 3:
        
            values = []
            
            for c in self.children:
                values.append(c.get_value())
                
            value = max(values)
                
        elif self.id == 4:
            
            value = self.value
            
        elif self.id == 5:
            
            if self.children[0].get_value() > self.children[1].get_value():
                value = 1
            else:
                value = 0
                
        elif self.id == 6:
         
            if self.children[0].get_value() < self.children[1].get_value():
                value = 1
            else:
                value = 0
                
        elif self.id == 7:
         
            if self.children[0].get_value() == self.children[1].get_value():
                value = 1
            else:
                value = 0
                
        return value
            
            
            
        
        
        
        

f = open('input.txt', 'r')
hex_string = f.read()

binary_string = bin(int(hex_string, 16))[2:]

node = Node(binary_string)

print(node.sum_version_numbers())
print(node.get_value())