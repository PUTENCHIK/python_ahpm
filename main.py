from models.Config import Config
from models.FileReader import FileReader
from models.Rational import Rational
from models.Matrix import Matrix


if __name__ == "__main__":
    options = FileReader.read_rows(Config.options_file_default)

    criteria = FileReader.read_rows(Config.criteria_file_default)

    matrix_2 = FileReader.read_matrices(Config.matrix_2_default)

    matrix_3 = FileReader.read_matrices(Config.matrix_3_default, len(options), len(criteria))

    print(options)
    print(criteria)
    print(matrix_2)

    for m in matrix_3:
        print(m)
