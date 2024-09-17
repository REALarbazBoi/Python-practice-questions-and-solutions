class Angle:

    def __init__(self, degree):
        self.degree = degree

    def __add__(self, ang):
        new = Angle(self.degree + ang.degree)
        return new

    def __str__(self):
        return "degree " + str(self.degree)

a1 = Angle(30)
a2 = Angle(45)
a3 = a1 + a2
# print(a1.degree + a2.degree)
print(a3)