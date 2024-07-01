# hw2.py
# Name: Min Soo Kang
# Collaborators: 
# References: 

def forLoops():
    """Prints 5, 9, 13, 17, 21 on separate lines
    """    
    for i in range(5):
        num = i + 5 + 3*i
        print(num)

def pay(hourly_wage, hours_worked):
    """Computes the employee's pay.

    Args:
        hourly_wage (Non-Negative Integer): represents an employee's hourly wage
        hours_worked (Non-Negative Integer): represents the number of hours the employee has worked

    Returns:
        float: the employee's earnings
    """
    if hours_worked > 40:
        return hourly_wage*40+1.5*hourly_wage*(hours_worked-40)
    return hourly_wage * hours_worked

def abbreviation(day):
    """Returns the abbreviated version of a day.

    Args:
        day (String): represents the day of the week

    Returns:
        String: the abberviation of given day
    """    
    return day[:2]

import math
def collision(x1,y1,r1,x2,y2,r2):
    """Returns true if there exists a collision.

    Args:
        x1 (float): x-coordinate of first circle
        y1 (float): y-coordinate of first circle
        r1 (float): radius of first circle
        x2 (float): x-coordinate of second circle
        y2 (float): y-coordinate of second circle
        r2 (float): radius of second circle

    Returns:
        bool: state of collision
    """    
    return r1 + r2 >= math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def partition(players):
    """Prints players with names that start with a letter between and including A and M.

    Args:
        players (list): list of players
    """
    for player in players:
        if (player[0] <= 'M'):
            print(player)


def lastF(first_name, last_name):
    """Returns the full name of the form '<Last>, <First Initial>'

    Args:
        first_name (String): first name
        last_name (String): last name

    Returns:
        String: full name
    """    
    return last_name + ', ' + first_name[0] + '.'


if __name__=='__main__':
   import doctest
   print( doctest.testfile('hw2TEST.py'))