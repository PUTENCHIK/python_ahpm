from pathlib import Path
from models.Matrix import Matrix


class FileReader:
    @staticmethod
    def read_rows(path: str) -> list:
        if not Path(path).is_file():
            raise FileNotFoundError

        arr = []
        with open(path, encoding="UTF-8") as file:
            for row in file:
                if row:
                    arr += [row.strip()]

        return arr

    @staticmethod
    def read_matrices(path: str, n: int = 0, expected_matrices: int = 1) -> Matrix | list[Matrix]:
        if not Path(path).is_file():
            raise FileNotFoundError

        with open(path, encoding="UTF-8") as file:
            if expected_matrices == 1:
                return Matrix(string="".join(file))
            else:
                arr = []
                strings = []
                for row in file:
                    if row.strip() != "":
                        strings += [row]
                        if len(strings) == n:
                            arr += [Matrix(string="".join(strings))]
                            strings = []
                if len(arr) != expected_matrices:
                    raise ValueError(f"In input file {path} are only {len(arr)} matrices instead of {expected_matrices}")

                return arr

