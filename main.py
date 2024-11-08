from models import HierarchyProcessMethod


if __name__ == "__main__":
    hpm = HierarchyProcessMethod("my")

    hpm.print_scores(check_matrices=True)
