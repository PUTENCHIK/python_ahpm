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
            self.den = den if den != 0 else 1

        self.simplify()

    def simplify(self):
        if self.den < 0:
            self.num *= -1
            self.den *= -1

        if self.num == 0:
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

    def __int__(self):
        return self.num // self.den

    def __float__(self):
        return self.num / self.den

    def __str__(self):
        return f"{self.num}/{self.den}"
