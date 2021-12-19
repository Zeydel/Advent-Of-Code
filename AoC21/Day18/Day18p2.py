def add(n1, n2):
    return '[' + n1 + ',' + n2 + ']'

def explode(number, index):
    
    right_bracket = -1
    
    for i in number[index:]:
        if number[i] == ']':
            right_bracket = i
            
    n1, n2 = [int(i) for i in number[index:right_bracket]]
    

def reduce(number):
    
    bracket = 0
    
    for i, c in number:
        if c == '[':
            bracket += 1
        elif c == ']':
            bracket -= 1
            
        if bracket == 5:
            explode(number, i)
            
# Open fil and read as lines
f = open('input.txt', 'r')
target = f.read().split('\n')

