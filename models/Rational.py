from typing import Self


class Rational:
    def __init__(self, num: int = 0, den: int = 1, string: str = None):
        if string is not None:
            if "/" in string:
                try:
                    self.num = int(string[:string.index("/")])
                    self.den = int(string[string.index("/")+1:])
                except ValueError:
                    raise ValueError(f"Wrong format of string rational: {string}")
            else:
                try:
                    self.num = int(string)
                    self.den = 1
                except ValueError:
                    self.num = 0
                    self.den = 0
                    # raise ValueError(f"Bad string for rational constructor: {string}")
        else:
            self.num = num
            self.den = den

        self.simplify()

    def simplify(self):
        if self.den < 0:
            self.num *= -1
            self.den *= -1

        if self.den == 0 or self.num == 0:
            self.den = 1
        else:
            a, b = abs(self.num), self.den
            while a != b:
                if a > b:
                    a -= b
                else:
                    b -= a

            self.num //= a
            self.den //= a
    
    def is_reverse(self, other: Self) -> bool:
        return self.num == other.den and self.den == other.num

    def __int__(self):
        return self.num // self.den

    def __float__(self):
        return self.num / self.den

    def __str__(self):
        return str(self.num) if self.den == 1 else f"{self.num}/{self.den}"

    def __add__(self, other: int | Self) -> Self:
        if isinstance(other, int):
            return self + Rational(other)
        elif isinstance(other, self.__class__):
            return Rational(self.num*other.den + other.num*self.den, self.den*other.den)
        else:
            raise NotImplementedError

    def __sub__(self, other: int | Self) -> Self:
        if isinstance(other, int) or isinstance(other, self.__class__):
            return self + other * -1
        else:
            raise NotImplementedError

    def __mul__(self, other: int | Self) -> Self:
        if isinstance(other, int):
            return Rational(self.num * other, self.den)
        elif isinstance(other, self.__class__):
            return Rational(self.num * other.num, self.den * other.den)
        else:
            raise NotImplementedError

    def __truediv__(self, other: int | Self) -> Self:
        if isinstance(other, int):
            return Rational(self.num, self.den * other)
        elif isinstance(other, self.__class__):
            return self * Rational(other.den, other.num)
        else:
            raise NotImplementedError

    def __eq__(self, other: int | float | Self) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            return float(self) == other
        elif isinstance(other, self.__class__):
            return self.num == other.num and self.den == other.den
        else:
            raise NotImplementedError
