# hw4.py
# Name: Min Soo Kang
# Collaborators: 
# References: 

def vowelIndex(str):
    """Returns the index of the first vowel that appears in the word.

    Args:
        str (String): given word that may or may not have vowels

    Returns:
        integer: index of the first vowel
    """    
    for i in range(len(str)):
        if str[i] in 'AEIOUaeiou':
            return i
    return -1

def flipCase(word):
    """Flips the uppercase characters to lowercase and vice versa in the given word.

    Args:
        word (String): given word to flip

    Returns:
        String: the new string flipped
    """    
    output_string = ""
    for c in word:
        if c.isupper():
            output_string += c.lower()
        else:
            output_string += c.upper()
    return output_string


def palindromes(sentence):
    """Finds all the palindromes in the given sentence.

    Args:
        sentence (String): given sentence

    Returns:
        list: list of palindromes
    """    
    output_list = []
    # Preprocessing
    for c in sentence:
        if c in '\"!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\"':
            sentence = sentence.replace(c, "")
    for word in sentence.split():
        if word[::-1].upper() == word.upper():
            output_list.append(word)
    return output_list

def squares(two_dimensional_list):
    """Given a 2-dimensional list, returns the number of perfect squares.

    Args:
        two_dimensional_list (2-dimensional list): the given 2-dimensional list

    Returns:
        integer: the number of perfect squares in the matrix
    """    
    count = 0
    row_size = len(two_dimensional_list)
    for row in range(row_size):
        col_size = len(two_dimensional_list[row])
        for col in range(col_size):
            if is_a_square(two_dimensional_list[row][col]):
                count += 1
    return count

def is_a_square(num):
    """Helper function to determine wheterh the given number is a perfect square.

    Args:
        num (integer): the given integer that may or may not be a perfect square

    Returns:
        boolean: returns true if the given number is a perfect square
    """    
    base = 0
    while base*base < num:
        base += 1
    return base * base == num

def rps(player_one, player_two):
    """Usage: rps(player_one, player_two). Simulate a game of rock paper scissors between two players. Returns 0 if tied, -1 if player_one wins, 1 if player_two wins.

    Args:
        player_one (String): represents player one's move
        player_two (String): represents player two's move

    Returns:
        integer: a flag indicating which players won, or if they tied
    """    
    winner = {
        'P': 'R',
        'S': 'P',
        'R': 'S'
    }
    if player_one == player_two:
        return 0
    elif winner[player_one] == player_two:
         return -1
    else:
        return 1

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))