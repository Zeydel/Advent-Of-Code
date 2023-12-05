# Read and parse the input
f = open('input.txt', 'r')
cards = f.read().split('\n')

# Dictionary for amount of each card number
card_amounts = {}

# Variable for the toal points
total_points = 0

# For every card
for i, card in enumerate(cards):
    
    # Count the card
    if i not in card_amounts:
        card_amounts[i] = 0    
    card_amounts[i] += 1
    
    # Process the string
    card = card.split(': ')[1]
    
    winning_numbers = [int(num) for num in card.split('|')[0].split()]
    own_numbers = [int(num) for num in card.split('|')[1].split()]
    
    # Counts for points and number of matches
    points = 0
    matches = 0
    
    # For every own number, check if it exists in the list of winning numbers
    for num in own_numbers:
        
        # If it exists, count it and add points
        if num in winning_numbers:
            matches += 1
            if points == 0:
                points = 1
            else:
                points *=2
                
    # Add the points to the total
    total_points += points
    
    # Add the winning cards to the counts
    for j in range(i+1, i+1+matches):
        
        if j not in card_amounts:
            card_amounts[j] = 0
        
        card_amounts[j] += card_amounts[i]
    
# Print the results
print(f'The total number of points is {total_points}')
print(f'The total number of cards is {sum(card_amounts.values())}')