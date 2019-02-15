import sympy
import random

class Degree_1_gen(object):
    def __init__(self):
        self.x = sympy.symbols('x')
        self.y = sympy.symbols('y')
        self.z = sympy.symbols('z')

    def Low_Any_Eq(self):
        n = random.randint(1,5)
        coefX= n * self.x
        simpleDegree1 = coefX + random.randint(1,10)
        expr = sympy.Eq(simpleDegree1, random.randint(1,10))
        return expr

    def Derivative_LOW_ANY(self):
        n = random.randint(1, 5)
        coefX = n * self.x
        simpleDegree1 = coefX + random.randint(1, 10)
        return simpleDegree1

    def High_Any_Eq(self):
        n = random.randint(5, 10)
        HcoefX = n * self.x
        HardDegree1 = HcoefX + random.randint(1, 30)
        expr = sympy.Eq(HardDegree1, random.randint(1, 30))
        return expr


    def Unsimplfied_LOW_ANY(self):
        n = random.randint(1, 5)
        coefX = n * self.x
        simpleDegree1 = coefX + random.randint(1, 10)

        G = random.randint(1, 5)
        GcoefX = G * self.x
        GsimpleDegree1 = GcoefX + random.randint(1, 10)

        expr = sympy.Eq(simpleDegree1, GsimpleDegree1)
        return expr

    def Unsimplfied_HIGH_ANY(self):
        n = random.randint(5, 10)
        HcoefX = n * self.x
        HardDegree1 = HcoefX + random.randint(1, 20)

        G = random.randint(5, 10)
        GHcoefX = G * self.x
        GHardDegree1 = GHcoefX + random.randint(1, 20)

        expr = sympy.Eq(HardDegree1, GHardDegree1)
        return expr

    def Low_Whole_Eq(self):
        # Ax + B = C
        n = random.randint(1, 5)
        r = random.randint(1, 5)
        coefX = n * self.x
        B = random.randint(1, 10)
        simpleDegree1 = coefX + B
        C = B + n * r
        expr = sympy.Eq(simpleDegree1, C)
        return expr

    def High_Whole_Eq(self):
        # Ax + B = C
        n = random.randint(5, 10)
        r = random.randint(1, 10)
        coefX = n * self.x
        B = random.randint(1, 20)
        simpleDegree1 = coefX + B
        C = B + n * r
        expr = sympy.Eq(simpleDegree1, C)
        return expr

    def Unsimplified_High_whole(self):
        # (n-r)x - rando = (n-r)rando - rando
        n = random.randint(9, 16)
        r = random.randint(1, 8)
        coefX = n * self.x
        HcoefX = r * self.x
        B = (n - r) * random.randint(1, 10)
        C = random.randint(1, 5)
        Right = coefX + C
        Left = HcoefX + C + B
        expr = sympy.Eq(Right, Left)
        return expr

    def Unsimplified_Low_whole(self):
        # (n-r)x - rando = (n-r)rando - rando
        n = random.randint(4, 6)
        r = random.randint(1, 3)
        coefX = n * self.x
        HcoefX = r * self.x
        B = (n - r) * random.randint(1, 4)
        C = random.randint(1, 5)
        Right = coefX + C
        Left = HcoefX + C + B
        expr = sympy.Eq(Right, Left)
        return expr

class Degree_2_gen(object):
    def __init__(self):
        self.x = sympy.symbols('x')
        self.y = sympy.symbols('y')
        self.z = sympy.symbols('z')

    def Derivative_2nd(self):
        n = random.randint(1, 5)
        coefX = n * self.x * self.x
        co = self.x * random.randint(1, 10)
        simpleDegree1 = coefX + co
        return simpleDegree1

    def Simple_DEGREE2(self):
        n = random.randint(1, 5)
        coefX = self.x * self.x
        simpleDegree1 = coefX
        expr = sympy.Eq(simpleDegree1, n * n)
        return expr

    def UNSimple_DEGREE2(self):
        n = random.randint(1, 5)
        coefX = n * self.x * self.x
        simpleDegree1 = coefX + random.randint(1, 5)
        expr = sympy.Eq(simpleDegree1, random.randint(6, 10))
        return expr


