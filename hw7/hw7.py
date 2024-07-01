# hw7.py
# Name: Min Soo Kang
# Collaborators: 
# References: 

class Volume:
    def __init__(self, value=0):
        self.value = self.validVolume(value)
    
    def validVolume(self, value):
        if value < 0: value = 0
        if value > 11: value = 11
        return value
    
    def __repr__(self):
        return f"Volume({self.value})"

    def __eq__(self, other_volume):
        return self.value == other_volume.value

    def set(self, value):
        self.value = self.validVolume(value)

    def get(self):
        return self.value

    def up(self, amount):
        self.value = self.validVolume(self.value + amount)

    def down(self, amount):
        self.value = self.validVolume(self.value - amount)

def partyVolume(file_path):
    file = open(file_path, 'r')
    initial_volume = float(file.readline().strip())
    v = Volume(initial_volume)
    adjustments = file.readlines()
    for command in adjustments:
        command = command.strip().split()
        value = command[-1]
        direction = command[0]
        if direction == 'U':
            v.up(float(value))
        elif direction == 'D':
            v.down(float(value))
    file.close()
    return v


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw7TEST.py'))