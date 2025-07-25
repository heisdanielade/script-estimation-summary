from typing import Callable

import pyfiglet
from colorama import init, Fore, Style
from tabulate import tabulate

from plane_client import PlaneClient
from estimator import Estimator

init(autoreset=True)


if __name__ == "__main__":
    ascii_art = pyfiglet.figlet_format("Plane.so", font="slant")
    print(ascii_art)

    client = PlaneClient()
    project = client.get_project_details()
    cycle = client.get_cycle_details()
    issues = client.get_issues_by_cycle()

    estimator = Estimator(issues=issues)
    TOTAL_ESTIMATION_POINTS = estimator.get_total_estimate_points()

    print("=" * 50)
    print(Fore.GREEN +
          f"📁 Project: \033[1m{project.get("name", "--")}\033[0m\n")
    print(Fore.GREEN + f"🔁 Cycle: \033[1m{cycle.get("name", "--")}\033[0m")
    print("-" * 50)

    print(Fore.GREEN +
          f"📝 Fetched \033[1m{len(issues)} issues\033[0m:\n")

    headers = [
        "Issue",
        "Priority",
        "Estimate Point",
        "Start Date",
        "Target Date",
        "Completed At"
    ]

    bold_headers = [Fore.YELLOW + f"{item}" +
                    Style.RESET_ALL for item in headers]

    check_availability: Callable[[str],
                                 str] = lambda val: val if val is not None else "n/a"

    def indicate_priority(value: str) -> str:
        """
        Return colored text based on issue priority level.
        """
        priority_map: dict = {
            "urgent": 4,
            "high": 3,
            "medium": 2,
            "low": 1,
            "none": 0
        }
        if priority_map.get(value, 0) == 4:
            return Fore.LIGHTRED_EX + value + Style.RESET_ALL
        if priority_map.get(value, 0) == 3:
            return Fore.LIGHTYELLOW_EX + value + Style.RESET_ALL
        if 0 < priority_map.get(value, 0) <= 2:
            return Fore.LIGHTBLUE_EX + value + Style.RESET_ALL
        if priority_map.get(value, 0) == 0:
            return value

        return value

    table = [
        (
            i.get('name'),
            indicate_priority(i.get('priority')),
            i.get('estimate_point')['value'],
            check_availability(i.get('start_date')),
            check_availability(i.get('target_date')),
            check_availability(i.get('completed_at'))
        )
        for i in issues
    ]

    print(tabulate(table, headers=bold_headers, showindex=range(
        1, len(table)+1), tablefmt="double_grid", numalign="center") + "\n")

    print(Fore.GREEN +
          f"✅ Total Estimation Points: \033[1m{TOTAL_ESTIMATION_POINTS} SP\033[0m")

    print("=" * 50)
