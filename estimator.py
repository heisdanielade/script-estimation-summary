class Estimator:
    """
    Perform operations on estimate points.
    Available Operations:
        GET TOTAL
    """

    def __init__(self, issues: list) -> None:
        self.issues = issues

    def get_total_estimate_points(self) -> int:

        return sum(
            int(item.get("estimate_point")['value'])
            for item in self.issues
        )
