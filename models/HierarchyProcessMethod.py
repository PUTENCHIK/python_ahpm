import pandas as pd
from pathlib import Path
from pprint import pprint

from models import Config, FileReader, Matrix
from models.Score import Score
from models.Exceptions import MatrixIsNotSymmetrical


class HierarchyProcessMethod:
    RC_coeffs = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
    m2_name = "matrix_2"
    
    def __init__(self, folder: str = Config.default_folder, ver_sym: bool = True) -> None:
        folder = f"{Config.files_folder}/{folder}"
        if not Path(folder).is_dir():
            raise ModuleNotFoundError(f"No folder {folder}")
        
        self.folder = folder        
        
        self.options = FileReader.read_rows(f"{folder}/{Config.file_names['options']}")
        self.criteria = FileReader.read_rows(f"{folder}/{Config.file_names['criteria']}")
        self.m2 = FileReader.read_matrices(f"{folder}/{Config.file_names['m2']}")
        self.m3 = FileReader.read_matrices(f"{folder}/{Config.file_names['m3']}",
                                           len(self.options),
                                           len(self.criteria))
        
        if ver_sym:
            self.verify_symmetry()
        
    def verify_symmetry(self) -> None:
        if not self.m2.is_symmetrical():
            raise MatrixIsNotSymmetrical
        
        for m in self.m3:
            if not m.is_symmetrical():
                raise MatrixIsNotSymmetrical
    
    def print(self) -> None:
        print(self.options)
        print(self.criteria)
        print(self.m2)
        for c, m in zip(self.criteria, self.m3):
            print(f"{c}:\n{m}")

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

    def calc_scores(self) -> dict:
        answer = dict()

        m2_vector = self.m2.priority_vector()
        lmax = self.m2.calc_lmax(m2_vector)
        ci = self.__class__.calc_ci(lmax, self.m2.size())
        cr = self.__class__.calc_cr(ci, self.m2.size())

        m2 = Score(lmax, ci, cr, m2_vector)
        answer[self.__class__.m2_name] = m2.to_json()

        for crit, matrix in zip(self.criteria, self.m3):
            vector = matrix.priority_vector()
            lmax = matrix.calc_lmax(vector)
            ci = self.__class__.calc_ci(lmax, matrix.size())
            cr = self.__class__.calc_cr(ci, matrix.size())

            answer[crit] = Score(lmax, ci, cr, vector).to_json()

        return answer
    
    def global_priority(self) -> dict:
        obj = dict()
        scores = self.calc_scores()
        
        for i, option in enumerate(self.options):
            obj[option] = 0
            for j, m2_pr in enumerate(scores[self.__class__.m2_name]['vector']):
                obj[option] += m2_pr * scores[self.criteria[j]]['vector'][i]
            obj[option] = round(obj[option], 3)
        
        return obj
    
    def check_matrix(self, matrix: Matrix, title: str = None, print_title: bool = False):
        if print_title:
            print(f"{title}:")
            
        for i in range(matrix.size()-2):
            for j in range(i+1, matrix.size()-1):
                for k in range(j+1, matrix.size()):
                    a_ij, a_jk, a_ik = matrix.values[i][j], matrix.values[j][k], matrix.values[i][k]
                    if a_ij * a_jk != a_ik:
                        print(f"({i+1},{j+1},{k+1}) | {a_ij} * {a_jk} = {a_ij*a_jk} != {a_ik}")
        print()
    
    def check_matrices(self):
        # scores = self.calc_scores()
        self.check_matrix(self.m2, "Матрица критериев")
        for crit, matrix in zip(self.criteria, self.m3):
            self.check_matrix(matrix, crit)

    def print_scores(self, cutted: bool = True, check_matrices = False):
        scores = self.calc_scores()

        matrix_2 = self.m2.to_float()
        for i in range(len(matrix_2)):
            matrix_2[i] += [scores[self.__class__.m2_name]['vector'][i]]
            
        crits = [crit[:6] for crit in self.criteria] if cutted else self.criteria
        print(pd.DataFrame(matrix_2, index=crits, columns=crits + ["Weights"]).to_string())
        pprint(scores[self.__class__.m2_name])
        if check_matrices:
            self.check_matrix(self.m2)
        print()

        for i, crit in enumerate(self.criteria):
            print(f"{crit}:")

            matrix = self.m3[i].to_float()
            for j in range(len(matrix)):
                matrix[j] += [scores[crit]['vector'][j]]

            indexes = [chr(65 + c) for c in range(len(matrix))]
            print(pd.DataFrame(matrix, index=indexes, columns=indexes + ["Weights"]).to_string())
            pprint(scores[crit])
            if check_matrices:
                self.check_matrix(self.m3[i])
            print()

        print("Global:")
        pprint(self.global_priority())
