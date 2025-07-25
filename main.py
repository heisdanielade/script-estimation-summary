from typing import Callable

import pyfiglet
from colorama import init, Fore
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
          f"📝 Fetched {len(issues)} issues in {cycle.get("name", "--")} cycle:\n")

    headers = [
        "Issue",
        "Priority",
        "Estimate Point",
        "Start Date",
        "Target Date",
        "Completed At"
    ]

    check_availability: Callable[[str],
                                 str] = lambda val: val if val is not None else "n/a"

    table = [
        (
            i.get('name'),
            i.get('priority'),
            i.get('estimate_point')['value'],
            check_availability(i.get('start_date')),
            check_availability(i.get('target_date')),
            check_availability(i.get('completed_at'))
        )
        for i in issues
    ]

    print(tabulate(table, headers=headers, showindex=range(
        1, len(table)+1), tablefmt="double_grid", numalign="center") + "\n")

    print(Fore.GREEN +
          f"✅ Total Estimation Points: \033[1m{TOTAL_ESTIMATION_POINTS} SP\033[0m")

    print("=" * 50)
