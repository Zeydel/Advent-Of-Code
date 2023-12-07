import re
import functools

def get_hand_value(hand):
        
    # Sort the list of cards to better regex it
    handSorted = ''.join(sorted(list(hand)))
    
    # The case where all cards are similar, like AAAAA
    if re.findall(r'(\w)\1{4}', handSorted):
        return 7

    # The case where 4 cards are similar, like AAAAB or BAAAA    
    if re.findall(r'(\w)\1{3}', handSorted):
        return 6
    
    # The case where 2 cards are similar and three other cards are similar. Like AABBB or AAABB
    if re.findall(r'(\w)\1{1}(\w)\2{2}', handSorted) or re.findall(r'(\w)\1{2}(\w)\2{1}', handSorted):
        return 5
    
    # The case where 3 cards are similar. Like AAABC or ABCCC
    if re.findall(r'(\w)\1{2}', handSorted):
        return 4
    
    # The case where two pairs of cards are similar, like AABBC, AABCC or ABBCC
    if re.findall(r'(\w)\1{1}(\w)\2{1}', handSorted) or re.findall(r'(\w)\1{1}\w(\w)\2{1}', handSorted):
        return 3

    # The case where two cards are similar, like AABCD, ABBCD, ABCCD or ABCDD
    if re.findall(r'(\w)\1{1}', handSorted):
        return 2
    
    # The case where all cards are different
    return 1

# Function to get best hand with wildcards
def get_best_hand(hand):
    
    # If there are no wildcards, just retiurn the hand
    if 'J' not in hand:
        return hand
    
    # List of replacements
    replacements = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    
    # Vars to keep track of best hand
    max_val = -1
    best_hand = ''
    
    # For every replacement
    for r in replacements:
        
        # Replace all jokers. A bit of thinking shows that it is always
        # beneficial to replace all wildcards with the same card
        val = get_hand_value(hand.replace('J', r))
        
        # If we have a new best, remember it
        if val > max_val:
            max_val = val
            best_hand = hand.replace('J', r)
                    
    # Return the best hand
    return best_hand

# Get the value of a card
def get_card_value(card):
    
    if card.isdigit():
        return int(card)
    
    values = {'T':10,
              'J':11,
              'Q':12,
              'K':13,
              'A':14}
    
    return values[card]

# Get the value of a card, with new value of wildcards
def get_card_value_wildcard(card):
    
    if card.isdigit():
        return int(card)
    
    values = {'T':10,
              'J':1,
              'Q':12,
              'K':13,
              'A':14}
    
    return values[card]

# Function to compare two hands
def compare_hands(hand1, hand2):
    
    hand1Val = get_hand_value(hand1[0])
    hand2Val = get_hand_value(hand2[0])
    
    # If the two hands have different values, return the difference
    if hand1Val != hand2Val:
        return hand1Val - hand2Val
    
    # Otherwise, go through them pairwise and return the first difference in card value 
    for a, b in zip(hand1[0], hand2[0]):
        if a != b:
            return get_card_value(a) - get_card_value(b)
        
# As above, but using the wildcard versions of functions
def compare_hands_wildcard(hand1, hand2):
    
    hand1Val = get_hand_value(hand1[2])
    hand2Val = get_hand_value(hand2[2])
    
    if hand1Val != hand2Val:
        return hand1Val - hand2Val
    
    for a, b in zip(hand1[0], hand2[0]):
        
        if a != b:
            return get_card_value_wildcard(a) - get_card_value_wildcard(b)
    
# Read and parse the input
f = open('input.txt', 'r')
hands = f.read().split('\n')

# Parse the input
hands = [(hand.split()[0], int(hand.split()[1])) for hand in hands]


# Init vars for the results
winnings = 0
winnings_wildcard = 0

# Sort the hands based on the comparison function
hands = sorted(hands, key=functools.cmp_to_key(compare_hands))

# Go through the sorted hands and calculate the winnings
for rank, hand in enumerate(hands, start=1):
    
    winnings += rank * hand[1]
    
# For each hand, calculate the best hand obtainable by replacing wildcards
for i, h in enumerate(hands):
    
    hands[i] = (h[0], h[1], get_best_hand(h[0]))

# Sort hands again, based on best hand
hands = sorted(hands, key=functools.cmp_to_key(compare_hands_wildcard))

# Calculate new total winnings
for rank, hand in enumerate(hands, start=1):
    
    winnings_wildcard += rank * hand[1]
    
# Print the results
print(f'The total winnings are {winnings}')
print(f'Playing with wildcards, the total winnings are {winnings_wildcard}')











