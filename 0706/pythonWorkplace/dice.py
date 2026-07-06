from random import randint

class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._size = 30
        self._value = 1
        
    def read_dice(self):
        return self._value
    
    def print_dice(self):
        print("dice num = {0} ".format(self._value))
        
    def roll_dice(self):
        self._value = randint(1,6)
        
d = Dice(100, 100)
d.roll_dice()
d.print_dice()