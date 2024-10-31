from pprint import pprint
from models import (
    Config,
    FileReader,
    HierarchyProcessMethod
)


if __name__ == "__main__":
    hpm = HierarchyProcessMethod("my")
    
    # hpm.print()
    
    # pprint(hpm.calc_scores())
    
    pprint(hpm.global_priority())
