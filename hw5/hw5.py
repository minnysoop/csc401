# hw5.py
# Name: Min Soo Kang
# Collaborators: 
# References: 

def doubleVowel(word):
    """Returns true if there are two adjacent vowels in the word.

    Args:
        word (String): given word

    Returns:
        boolean: whether the word contains adjacent vowels
    """    
    word = word.upper()
    prev = word[0]
    i = 1
    while i < len(word):
        if prev in "AEIOU" and word[i] in "AEIOU":
            return True
        else:
            prev = word[i]
        i += 1
    return False

def numPairs(target, numlist):
    """Returns the number of pairs in numlist that add up to target. Pairs are tuples of different indices.

    Args:
        target (integer): target to sum to
        numlist (list): list of integers

    Returns:
        integer: the number of pairs that sum up to target
    """    
    count = 0
    visited = []
    for i in range(len(numlist)):
        for j in range(len(numlist)):
            if numlist[i] + numlist[j] == target and (i,j) not in visited and (j,i) not in visited and i != j:
                count += 1
                visited.append((i,j))
    return count

def hideShow(input, mask):
    """Masks the given input given. Both input and mask are of the same length.

    Args:
        input (String): word to mask
        mask (String): mask to apply

    Returns:
        String: new masked string
    """    
    output = ""
    i = 0
    while i < len(mask):
        if mask[i] == '0':
            output += '#'
        else:
            output += input[i]
        i += 1
    return output

def clean(dirty_word):
    """Removes leading and trailing spaces, tabs, and new lines of the given string.

    Args:
        dirty_word (String): given word

    Returns:
        String: supplied word without excess spaces, tabs, and new lines
    """    
    while dirty_word and (dirty_word[0] in [' ', '\t', '\n']):
        dirty_word = dirty_word[1:]
    while dirty_word and (dirty_word[-1] in [' ', '\t', '\n']):
        dirty_word = dirty_word[:-1]
    return dirty_word

def sequence(start):
    """Simulates a convergent sequence given a starting point.

    Args:
        start (integer): the starting point of the sequence
    """    
    while True:
        print(start)
        if start == 1: 
            break
        elif start%2 == 0:
            start //= 2
        else:
            start += 1

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))