class Score:
    def __init__(self,
                 lmax: float = None,
                 ci: float = None,
                 cr: float = None,
                 vector: list[float] = None):
        self.lmax = lmax
        self.CI = ci
        self.CR = cr
        self.vector = vector

    def to_json(self, r: int = 3) -> dict:
        return {
            "lmax": round(self.lmax, r),
            "CI": round(self.CI, r),
            "CR": round(self.CR, r),
            "vector": [round(e, r) for e in self.vector]
        }
