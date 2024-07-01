# hw3.py
# Name: Min Soo Kang
# Collaborators: 
# References: 

def cheer(team_name):
    """Prints a cheer for the given team name,

    Args:
        team_name (String): team's name
    """
    chant = " ".join(list(team_name.upper()))
    print(f"How do you spell winner?\nI know, I know!\n{chant} !\nAnd that's how you spell winner!\nGo {team_name}!")

def vowelCount(word):
    """Print out the number of vowels in the word.

    Args:
        word (String): any word
    """    
    vowel_count = {"a":0,"e": 0,"i":0,"o":0,"u":0}
    for c in word:
        if c in vowel_count.keys():
            vowel_count[c] += 1
    print(f'a, e, i, o, and u appear, respectively, {vowel_count["a"]}, {vowel_count["e"]}, {vowel_count["i"]}, {vowel_count["o"]}, {vowel_count["u"]} times.')

def crypto(file_name):
    """Replaces the word "secret" with "xxxxxx". Prints the result.

    Args:
        file_name (String): path to the file
    """    
    with open(file_name, "r") as file:
        text = file.read()
        print(text.replace("secret", "xxxxxx"))

def links(html_file):
    """Returns the number of links in the html file

    Args:
        html_file (String): path to HTML file

    Returns:
        Non-negative Integer: number of links in the file
    """    
    with open(html_file, "r") as file:
        text = file.read()
        count = text.count("</a>")
        return count

def duplicate(file_name):
    """Determines whether the provided file contains duplicate words.

    Args:
        file_name (String): path to file

    Returns:
        boolean: whether there are duplicate words in the file or not
    """    
    wordList = []
    with open(file_name, "r") as file:
        words = file.read()

        # Preprocessing
        words = words.upper()
        for c in words:
            if c in '\"!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\"':
                words = words.replace(c, "")
        
        for w in words.split():
            if w in wordList:
                return True
            else:
                wordList.append(w)
        return False


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))