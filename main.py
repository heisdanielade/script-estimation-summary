from plane_client import PlaneClient
import pyfiglet
from colorama import init, Fore
init(autoreset=True)


# def main() -> None:
#     ascii_art = pyfiglet.figlet_format("Cycle Info", font="slant")
#     print(ascii_art)

#     while True:
#         try:
#             command = input("script>> ").strip()
#             if command in ("exit", "quit", "q"):
#                 print("\nGoodbye!\n")
#                 break
#         except (KeyboardInterrupt, EOFError):
#             print("\nGoodbye!\n")
#             break


if __name__ == "__main__":
    ascii_art = pyfiglet.figlet_format("Plane.so", font="slant")
    print(ascii_art)

    client = PlaneClient()

    issues = client.get_issues_by_cycle()
    estimate_map = None  # client.get_estimate_value_map()
    TOTAL_ESTIMATION_POINTS = None

    print("=" * 50)


    print(Fore.GREEN +
          f"Fetched {len(issues)} issues:\n")

    for issue in issues:
        print(Fore.YELLOW +
              f" - {issue.get('name')} (Estimate: {issue.get('estimate_point', 0)} SP)")

    print("-" * 50)
    print(Fore.GREEN +
          f"✅ Total Estimation Points: {TOTAL_ESTIMATION_POINTS} SP")
    print("=" * 50)

    # for issue in issues:
    #     est_id = issue.get("estimate_point")
    #     points = estimate_map.get(est_id, 0)  # default to 0 if not found
    #     print(f"- {issue.get('name')} (Estimate: {points} SP)")
