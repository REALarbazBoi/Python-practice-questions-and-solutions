class Rational:

    def __init__(self,p = 1, q = 1):
        self.p = p
        self.q = q

    def __add__(self, other):
        p = self.p * other.q + self.q * other.p
        q = self.q * other.q
        sum1= Rational(p,q)
        return sum1

    def __sub__(self, other):
        p = self.p * other.q - self.q * other.p
        q = self.q * other.q
        sub1 = Rational(p, q)
        return sub1

    def __str__(self):
        return (str(self.p) + "/" + str(self.q))
r1 = Rational(2,3)
r2 = Rational(1,2)
r3 = r1 + r2
print(r3)