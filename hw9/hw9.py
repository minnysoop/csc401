# hw9.py
# Name: Min Soo Kang
# Collaborators: 
# References:

class Stack(list):
    def __init__(self, collection=None):
        if collection is not None:
            list.__init__(self, collection)
        else:
            list.__init__(self)
    
    def __repr__(self):
        return f"Stack({super().__repr__()})"

    def push(self, value):
        self.append(value)

    def pop(self):
        if not self.isEmpty():
            return super().pop()

    def isEmpty(self):
        return len(self) == 0

def parenthesesMatch(sequence):
    openning_brackets = Stack()
    for i in sequence:
        if i == '[' or i == '(' or i == '{':
            openning_brackets.push(i)
        else:
            if openning_brackets.isEmpty():
                return False
            else:
                top = openning_brackets.pop()
                if i == ']' and top != '[' or i == ')' and top != '(' or i == '}' and top != '{':
                    return False
    if not openning_brackets.isEmpty():
        return False
    return True

if __name__=='__main__': 
    import doctest 
    print(doctest.testfile( 'hw9TEST.py'))