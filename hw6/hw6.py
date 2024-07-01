# hw6.py
# Name: Min Soo Kang
# Collaborators: 
# References: 

def interleaved(list1, list2):
    """Merges two sorted sequences

    Args:
        list1 (list): list of sorted numbers
        list2 (list): list of sorted numbers

    Returns:
        list: merged list of sorted numbers
    """    
    i,j = 0,0
    output = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            output.append(list2[j])
            j += 1
        else:
            output.append(list1[i])
            i += 1
    output.extend(list1[i:])
    output.extend(list2[j:])
    return output

def primeFac(num):
    """Computes the prime factorization of num

    Args:
        num (integer): the number to factor

    Returns:
        list: list ocntaining prime factors
    """    
    prime_factors = []
    while num % 2 == 0:
        prime_factors.append(2)
        num //= 2
    i = 3
    while i <= num:
        while num % i == 0:
            prime_factors.append(i)
            num //= i
        i += 2
    return prime_factors

def piggyBank(coins):
    """Returns the total count of coins and total value of the bank.

    Args:
        coins (list): list of characters representing the number of coins

    Returns:
        integer: the total value in the bank
    """    
    return {'Q': coins.count('Q'), 'D': coins.count('D'), 'N': coins.count('N'), 'P': coins.count('P')}, 25*coins.count('Q') + 10*coins.count('D') + 5*coins.count('N') + coins.count('P')

import random
def roll():
    """Simulates rolling two dice and returning their sum.

    Returns:
        integer: the sum of two rolled dice
    """    
    return random.randrange(1,7) + random.randrange(1,7)

def craps():
    """Plays a game of craps.

    Returns:
        integer: 0 if lost, 1 if won
    """    
    first_roll = roll()
    if first_roll == 7 or first_roll == 11:
        return 1
    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        return 0
    
    while True:
        next_roll = roll()
        if next_roll == first_roll: 
            return 1
        if next_roll == 7: 
            return 0
        
def testCraps(games):
    """Simulates some number of games of Craps.

    Args:
        games (integer): number of games to play

    Returns:
        float: the ratio between wins and losses
    """    
    won = 0
    i = 1
    while i <= games:
        won += craps()
        i += 1
    return won/games

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py'))