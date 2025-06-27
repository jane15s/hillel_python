"""
Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання, віднімання та множення
для екземплярів цього класу.
"""

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Illegal value of the denominator")
        self.a = a
        self.b = b
        # self.__reduce()

    # def __reduce(self):
    #     def gcd(a, b):
    #         if a == 0:
    #             return b
    #         elif b == 0:
    #             return a
    #         elif a >= b:
    #             return gcd(a % b, b)
    #         else:
    #             return gcd(a, b % a)
    #
    #     sign = 1
    #     if (self.a > 0 > self.b) or \
    #             (self.a < 0 < self.b):
    #         sign = -1
    #     a, b = abs(self.a), abs(self.b)
    #     c = gcd(a, b)
    #     self.a = sign * (a // c)
    #     self.b = b // c

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
