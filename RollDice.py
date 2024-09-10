from random import *

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def rolldice(self):
        return randint(1, self.sides)

d = Dice(6)
print(d.rolldice())
print(d.rolldice())
print(d.rolldice())