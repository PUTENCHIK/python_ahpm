from models.Rational import Rational
from models.Config import Config


class Matrix:
    def __init__(self, n: int = 0, m: int = 0, string: str = None):
        if string is not None:
            self.values = []
            for row in string.split("\n"):
                row = row.strip()
                if row != "":
                    self.values += [[Rational(string=elem) for elem in row.replace("\t", " ").split(" ")]]
        else:
            self.values = [[Rational() for _ in range(m)] for _ in range(n)]

    def __str__(self):
        s = ""
        for i, row in enumerate(self.values):
            s += "[{}]\n".format("\t".join([str(elem) for elem in row]))
            # s += "\t\t".join([str(elem) for elem in row]) + "\n"

        return s
