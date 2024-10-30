from pprint import pprint
from models import (
    Config,
    FileReader,
    HierarchyProcessMethod
)


if __name__ == "__main__":
    options = FileReader.read_rows("files/opt_ex.txt")
    criteria = FileReader.read_rows("files/crit_ex.txt")
    matrix_2 = FileReader.read_matrices("files/m2_ex.txt")
    matrices_3 = FileReader.read_matrices("files/m3_ex.txt", len(options), len(criteria))

    # options = FileReader.read_rows(Config.options_file_default)
    # criteria = FileReader.read_rows(Config.criteria_file_default)
    # matrix_2 = FileReader.read_matrices(Config.matrix_2_default)
    # matrices_3 = FileReader.read_matrices(Config.matrices_3_default, len(options), len(criteria))

    answer = HierarchyProcessMethod.calc_scores(
        options=options,
        criteria=criteria,
        matrix_2=matrix_2,
        matrices_3=matrices_3
    )

    pprint(answer)

