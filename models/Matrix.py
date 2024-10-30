from typing import Self
from models.Rational import Rational
from models.Config import Config
from models.Exceptions import MatrixIsNotSquare


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

    def __len__(self) -> int:
        return len(self.values)

    def __mul__(self, other: list[float]) -> list[list[float]]:
        return [[float(elem)*other[j] for j, elem in enumerate(row)] for row in self.values.copy()]

    def size(self) -> int:
        return len(self.values)

    def is_square(self) -> bool:
        n = self.size()
        for i in range(n):
            if len(self.values[i]) != n:
                return False
        return True

    def priority_vector(self) -> list:
        if not self.is_square():
            raise MatrixIsNotSquare

        arr = []
        n = self.size()
        for i in range(n):
            p = 1
            for j in range(n):
                p *= float(self.values[i][j])
            arr += [p**(1/n)]

        s = sum(arr)
        return [e/s for e in arr]

    def calc_lmax(self, vector: list = None) -> float:
        if vector is None:
            vector = self.priority_vector()

        matrix = self * vector
        lmax = sum([sum(row) for row in matrix])

        return lmax
