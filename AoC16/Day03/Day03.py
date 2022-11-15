# Need numpy for array manipulation
import numpy as np

# Takes an array of length 3, and outputs if the triangle is possible
def isPossible(triangle):
    triangle = sorted(triangle)
    return triangle[0] + triangle[1] > triangle[2]

# Open input and read as 2d array of integers
f = open('input.txt', 'r')
triangles = np.array([[int(i) for i in l.split()] for l in f.read().split('\n')])

# Count the number of possible triangles when going vertically
possibleCounterHorizontal = sum([isPossible(t) for t in triangles])

# Count the number of possible triangles when going horizontally
possibleCounterVertical = 0
for i in range(0,len(triangles),3):
    for j in range(3):
        if isPossible(triangles[i:i+3,j]):
            possibleCounterVertical +=1

# Print the results
print(f'There are {possibleCounterHorizontal} when going horizontally')
print(f'There are {possibleCounterVertical} when going vertically')