# hw8.py
# Name: Min Soo Kang
# Collaborators: 
# References: Chapter 8 of Introduction to Computing using Python by Perkovic

class Pizza:
    def __init__(self, size='M', toppings=None):
        self.size = size
        self.toppings = toppings if toppings is not None else set()

    def __repr__(self):
        return f"Pizza('{self.size}',{self.toppings})"

    def __eq__(self, other_pie):
        return self.size == other_pie.size and self.toppings == other_pie.toppings

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def addTopping(self, topping):
        self.toppings.add(topping)

    def removeTopping(self, topping):
        self.toppings.remove(topping)

    def price(self):
        pie_price = {'S': 6.25, 'M': 9.95, 'L': 12.95}
        toppings_price = {'S': 0.70, 'M': 1.45, 'L': 1.85}
        return pie_price[self.size] + len(self.toppings)*toppings_price[self.size]

def orderPizza():
    print("Welcome to Python Pizza!")
    pizza = None
    while True:
        size = input("What size pizza would you like (S,M,L): ")
        pizza = Pizza(size=size)
        while True:
            t = input("Type topping to add (or Enter to quit): ")
            if t == '':
                break
            else:
                pizza.addTopping(t)
        cost = pizza.price()
        print("Thanks for ordering!")
        print(f"Your pizza costs ${cost}")
        break
    return pizza

if __name__=='__main__': 
    import doctest 
    print(doctest.testfile( 'hw8TEST.py'))