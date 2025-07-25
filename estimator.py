class Estimator:
    def __init__(self, issues: list) -> None:
        self.issues = issues

    def get_total_estimate_points(self) -> float:
        total: float = 0

        for item in self.issues:
            total += float(item.get("estimate_point")["value"])

        return total
