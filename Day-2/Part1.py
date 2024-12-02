from get_input import get_input


def check_report(report: list[int]) -> bool:
    inc = report[0] < report[1]
    for i in range(len(report) - 1):
        meow = abs(report[i] - report[i + 1])
        if meow > 3 or meow < 1:
            return False
        if (report[i] > report[i + 1]) if inc else (report[i] < report[i + 1]):
            return False
    return True


def summarize(data: list[list]) -> int:
    return sum(1 for i in data if check_report(i))


if __name__ == "__main__":
    print(summarize(get_input("input")))
