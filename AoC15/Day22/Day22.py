# Need to copy the state a bunch of times
import copy

# Class representing a state, featuring all the variables needed
class state:
    playerHp = 50
    playerMana = 500
    playerArmor = 0
    playersTurn = True
    
    bossHp = -1
    bossDamage = -1
    
    shieldTimer = 0
    poisonTimer = 0
    rechargeTimer = 0
    
    manaSpent = 0
    
# Functions for each spell. Returns a new state with the spell applied
def magicMissile(state):
    newState = copy.copy(state)
    newState.bossHp -= 4
    return newState

def drain(state):
    newState = copy.copy(state)
    newState.bossHp -= 2
    newState.playerHp += 2
    return newState

def shield(state):
    newState = copy.copy(state)
    newState.shieldTimer = 6
    return newState

def poison(state):
    newState = copy.copy(state)
    newState.poisonTimer = 6
    return newState

def recharge(state):
    newState = copy.copy(state)
    newState.rechargeTimer = 5
    return newState

# Function for the boss turn. Returns a new state
def bossTurn(state):
    newState = copy.copy(state)
    if state.shieldTimer > 0:
        newState.playerHp -= (newState.bossDamage-7)
    else: newState.playerHp -= newState.bossDamage
    return newState

# Resolves and counts down all the effects. Returns a new state
def resolveEffects(state, hardmode = False):
    newState = copy.copy(state)
    
    if hardmode and state.playersTurn:
        newState.playerHp -= 1
    
    if state.shieldTimer > 0:
        newState.shieldTimer -= 1
    if newState.poisonTimer > 0:
        newState.bossHp -= 3
        newState.poisonTimer -= 1
    if newState.rechargeTimer > 0:
        newState.playerMana += 101
        newState.rechargeTimer -= 1

    return newState

# Based on a state, gets the set of next possible states
def getNextTurns(state):

    # Init empty    
    nextTurns = set()
    
    # If it is the boss's turn, apply the boss turn and return the next state
    if not state.playersTurn:
        nextTurn = bossTurn(state)
        nextTurn.playersTurn = True
        nextTurns.add(nextTurn)
        return nextTurns

    
    # Else add all effects than can be added to the next turns set
    for k in effectMap:
        if k < state.playerMana:
            if k == 113 and state.shieldTimer > 0:
                continue
            if k == 173 and state.poisonTimer > 0:
                continue
            if k == 229 and state.rechargeTimer > 0:
                continue
            nextTurn = effectMap[k](state)
            nextTurn.manaSpent += k
            nextTurn.playerMana -= k
            nextTurn.playersTurn = False
            nextTurns.add(nextTurn)
            
    return nextTurns
    
# Functions to determine whether the player has lost or won
def playerLost(state):
    return state.playerHp <= 0

def playerWon(state):
    return state.bossHp <= 0

# Maps costs to spells
effectMap = {
    53 : magicMissile,
    73 : drain,
    113: shield,
    173: poison,
    229: recharge
    }

## Read input and parse
f = open('input.txt', 'r')
strings = f.read().split('\n')

# Define the inital state
initialState = state()
initialState.bossHp = int(strings[0].split(' ')[2])
initialState.bossDamage = int(strings[1].split(' ')[1])

# Add it to the set of unexplored states
unexplored = {initialState}
best = float('inf')

# While there are states to explare, do a turn and get
# all possible next turns to the set of unexplored states
while len(unexplored) > 0:
    cur = unexplored.pop()
    cur = resolveEffects(cur)
    
    # If we have surpassed the best cost, no need to seach further
    if cur.manaSpent > best:
        continue
    
    # If we have lost, no need to search further
    if playerLost(cur):
        continue
    
    # If we have won, no need to seach further. But check if we have gotten a new best
    if playerWon(cur):
        if cur.manaSpent < best:
            best = cur.manaSpent
        continue
    
    # Add the next states to the set
    unexplored |= getNextTurns(cur)
    
# Do the same thing again, but on hard mode
initialState = state()
initialState.bossHp = int(strings[0].split(' ')[2])
initialState.bossDamage = int(strings[1].split(' ')[1])

unexplored = {initialState}
bestHardMode = float('inf')

while len(unexplored) > 0:
    cur = unexplored.pop()
    cur = resolveEffects(cur, True)
    
    if cur.manaSpent > bestHardMode:
        continue
    
    if playerLost(cur):
        continue
    
    if playerWon(cur):
        if cur.manaSpent < bestHardMode:
            bestHardMode = cur.manaSpent
        continue
    
    
    unexplored |= getNextTurns(cur)
    

print(f'The least mana you can spend to win is {best}')
print(f'The least mana you can spend to win in hardmode is {bestHardMode}')
