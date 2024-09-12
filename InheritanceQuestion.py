import math
class Polygon:

    def __init__(self, no_sides, *sides):
        self.no_sides = no_sides
        self.sides = sides

class Triangle:

    def __init__(self, no_sides, *sides):
        Polygon.__init__(self, no_sides, *sides)

    def area(self):
        a, b, c = self.sides

        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area

t1 = Triangle(3, 10,15,9)
print(t1.area())


