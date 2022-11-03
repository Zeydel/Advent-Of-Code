# Imports to do smart things
import math
from itertools import combinations
from itertools import product

weapons = [
    (8,4,0),  # Dagger
    (10,5,0), # Shortsword
    (25,6,0), # Warhammer
    (40,7,0), # Longsword
    (74,8,0)  # Greataxe
    ]

armor = [
    (13, 0,1),# Leather
    (31, 0,2),# Chainmail
    (53, 0,3),# Splintmail
    (75, 0,4),# Bandemail
    (102,0,5) # Platemail
    ]

rings = [
    (25, 1,0),# Damage +1
    (50, 2,0),# Damage +2
    (100,3,0),# Damage +3
    (20 ,0,1),# Defense +1
    (40 ,0,2),# Defense +2
    (80,0,3)  # Defense +3
    ]

# Function to determine if a player wins the battle given two tuples of
# structure (HP, damage, armor)
def winsBattle(player, boss):
    
    # Extract the values
    playerHp, playerDamage, playerArmor = player[0], player[1], player[2]
    bossHp, bossDamage, bossArmor = boss[0], boss[1], boss[2]
    
    # Calculate the rounds needed to kill the player and boss
    roundsToKillPlayer = math.ceil(playerHp/(max(1, bossDamage-playerArmor)))
    roundsToKillBoss = math.ceil(bossHp/(max(1, playerDamage-bossArmor)))
    
    # Returns true if player kills the boss before boss kills the player
    # If they are equal, the player wins as he goes first
    return roundsToKillPlayer >= roundsToKillBoss

# Get all the possible weapon indices
def getPossibleWeapons(weapons):
    return [i for i, w in enumerate(weapons)]
    
# Get all the possible armor indeces including -1 signifying no armor
def getPossibleArmor(armor):
    return [i for i, a in enumerate(armor)] + [-1]

# Get all possible ring combinations, including no rings
def getPossibleRings(rings):
    return combinations([i for i, r in enumerate(rings)] + [-1, -1], 2)

# Get all combinations of weapon, armor and rings
def getEquipmentCombinations(weapons, armor, rings):
    return list(product(getPossibleWeapons(weapons), getPossibleArmor(armor), getPossibleRings(rings)))

# Calculates the cost of a combination
def getCombinationCost(combination):

    # Adds the cost of the weapon
    cost = weapons[combination[0]][0]
    
    # Adds the cost of armor if there is one
    if not combination[1] == -1:
        cost += armor[combination[1]][0]
        
    # Adds the cost of rings if they exist
    if not combination[2][0] == -1:
        cost += rings[combination[2][0]][0]
    if not combination[2][1] == -1:
        cost += rings[combination[2][1]][0]
                
    # Return the cost
    return cost

# Calculates the players stats
def getStats(combination):
    
    # Init as zero
    playerDamage, playerArmor = 0, 0
    
    # Adds weapon damage
    playerDamage += weapons[combination[0]][1]
    
    # Add amor if there is one
    if not combination[1] == -1:
        playerArmor += armor[combination[1]][2]
        
    # Add ring stats if they exist
    if not combination[2][0] == -1:
        playerDamage += rings[combination[2][0]][1]
        playerArmor += rings[combination[2][0]][2]
    if not combination[2][1] == -1:
        playerDamage += rings[combination[2][1]][1]
        playerArmor += rings[combination[2][1]][2]
        
    # Return the stats as a tuple
    return (100, playerDamage, playerArmor)
    
# Read input and parse
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Extract the boss values
bossHp = int(strings[0].split(' ')[2])
bossDamage = int(strings[1].split(' ')[1])
bossArmor = int(strings[2].split(' ')[1])

# Init limit values
bestCost = float('inf')
worstCost = float('-inf')

# Go through every combination
for c in getEquipmentCombinations(weapons, armor, rings):
    # Calculate its cost
    cost = getCombinationCost(c)
    
    # If cost is below current best cost, check if we win. Save new value
    # if we do
    if cost < bestCost and winsBattle(getStats(c), (bossHp, bossDamage, bossArmor)):
        bestCost = cost
        
    # If cost is more than worst cost, check if we lose. Save new value
    # if we do
    if cost > worstCost and not winsBattle(getStats(c), (bossHp, bossDamage, bossArmor)):
        worstCost = cost
        
print(f'The least money we can spend and win is {bestCost}')
print(f'The most money we can spend and lose is {worstCost}')
