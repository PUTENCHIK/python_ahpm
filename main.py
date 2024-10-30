from models import (
    Config,
    FileReader,
    Matrix,
    Rational
)


if __name__ == "__main__":
    options = FileReader.read_rows("files/opt_ex.txt")

    criteria = FileReader.read_rows("files/crit_ex.txt")

    matrix_2 = FileReader.read_matrices("files/m2_ex.txt")

    matrix_3 = FileReader.read_matrices("files/m3_ex.txt", len(options), len(criteria))

    # print(options)
    # print(criteria)
    #
    # print(matrix_2)
    #
    # for m in matrix_3:
    #     print(m)

    print(matrix_2.priority_vector())

    for m in matrix_3:
        print(m)
        print(m.priority_vector())
        print()
