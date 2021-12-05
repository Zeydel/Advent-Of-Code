import numpy as np

# Class to represent the bingo board
class Board:
    
    # Create board from numbers input. Create matrices for numbers and hits
    def __init__(self, numbers_input):
        self.numbers = self.parse_numbers(numbers_input)
        self.hits = np.zeros((5,5), dtype=bool)
        
    # Function to parse a list of strings into a 2d array of numbers
    def parse_numbers(self, numbers_input):
        board = []
        for n in numbers_input:
            board.append([i for i in n.split()])
        return board
    
    # Function to mark a number on a board, if it exists
    def mark_number(self, number):
        
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i][j] == number:
                    self.hits[i][j] = True
    
    # Function to check if board has bingo
    def has_bingo(self):
        for i in range(len(self.numbers)):
            if all(self.hits[i]):
                return True
            if all([row[i] for row in self.hits]):
                return True
            
        return False
    
    # Functio to get the sum of all unmarked numbers on the board
    def get_score(self):
        
        score = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if not self.hits[i][j]:
                    score += int(self.numbers[i][j])
        return score
    
# Open file and read as lines. Sort out empty lines
f = open('input.txt', 'r')
lines = list(filter(lambda line: line, f.read().split('\n')))

# First line is the sequence of called numbers
numbers = lines[0]

# Create all the boards from chucks of lines
boards = []
for i in range(1, len(lines), 5):
    boards.append(Board(lines[i:i+5]))

# Init some variables that we need
first_winner_score = first_winner_number = -1
last_winner_score = last_winner_number = -1
last_board = False

# For each number
for n in numbers.split(','):
    
    # Go through every board
    for board in boards:
        
        #Mark the board
        board.mark_number(n)
        
        # If the board is the first to get bingo, save the relevant variables
        if board.has_bingo() and first_winner_score == -1:
            first_winner_score = board.get_score()
            first_winner_number = int(n)
            
        # If the board is the last to get bingo, save the relevant variables
        if board.has_bingo() and last_board:
            last_winner_score = board.get_score()
            last_winner_number = int(n)
    
    # Sort out all the boards that has gotten bingo
    boards = list(filter(lambda board: not board.has_bingo(), boards))
    
    # If there is only one board left, flip this bool
    if len(boards) == 1:
        last_board = True
        
# Print the output
print('The score of the first winner is ' + str(first_winner_number * first_winner_score))
print('The score of the last winner is ' + str(last_winner_number * last_winner_score))