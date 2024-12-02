from Part1 import check_report
from get_input import get_input


def problem_dampener(report: list[int]) -> bool:
    if not check_report(report):
        for i in range(len(report)):
            if check_report(report[:i] + report[i + 1:]):
                return True
        return False
    else:
        return True


def summarize(data: list[list]) -> int:
    return sum(1 for i in data if problem_dampener(i))


if __name__ == "__main__":
    print(summarize(get_input("input")))
