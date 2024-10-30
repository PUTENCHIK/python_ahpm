from models import Config
from models import Matrix
from models.Score import Score


class HierarchyProcessMethod:
    RC_coeffs = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]

    @classmethod
    def calc_ci(cls, lmax: float, n: int) -> float:
        """
        :param lmax: максимальное случайное число
        :param n: размерность матрицы
        :return: индекс согласованности
        """
        return (lmax - n)/(n - 1)

    @classmethod
    def calc_cr(cls, ci: float, n: int):
        """
        :param ci: индекс согласованности
        :param n: размерность матрицы
        :return: отношение согласованности
        """
        return ci / cls.RC_coeffs[n-1]

    @classmethod
    def calc_scores(cls,
                    options: list[str],
                    criteria: list[str],
                    matrix_2: Matrix,
                    matrices_3: list[Matrix]) -> dict:
        answer = dict()

        m2_vector = matrix_2.priority_vector()
        lmax = matrix_2.calc_lmax(m2_vector)
        ci = cls.calc_ci(lmax, matrix_2.size())
        cr = cls.calc_cr(ci, matrix_2.size())

        answer['matrix_2'] = Score(lmax, ci, cr, m2_vector).to_json()

        for i, matrix in enumerate(matrices_3):
            vector = matrix.priority_vector()
            lmax = matrix.calc_lmax(vector)
            ci = cls.calc_ci(lmax, matrix.size())
            cr = cls.calc_cr(ci, matrix.size())

            answer[criteria[i]] = Score(lmax, ci, cr, vector).to_json()

        return answer
