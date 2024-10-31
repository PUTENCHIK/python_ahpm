class Score:
    r = 3
    
    def __init__(self,
                 lmax: float = None,
                 ci: float = None,
                 cr: float = None,
                 vector: list[float] = None):
        self.lmax = lmax
        self.CI = ci
        self.CR = cr
        self.vector = vector

    def to_json(self) -> dict:
        return {
            "lmax": round(self.lmax, self.__class__.r),
            "ИС": round(self.CI, self.__class__.r),
            "ОС": round(self.CR, self.__class__.r),
            "vector": [round(e, self.__class__.r) for e in self.vector]
        }
