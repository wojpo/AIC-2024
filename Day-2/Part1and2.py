from get_input import get_input


def check_report(report: list[int]) -> int:
    errors = 0
    inc = report[0] < report[1]
    for i in range(len(report) - 1):
        meow = abs(report[i] - report[i + 1])
        if meow > 3 or meow < 1:
            errors += 1
        if (report[i] > report[i + 1]) if inc else (report[i] < report[i + 1]):
            errors += 1
    return errors


def summarize_part_1(data: list[list]) -> int:
    return sum(1 for i in data if check_report(i) == 0)

def summarize_part_2(data: list[list]) -> int:
    return sum(1 for i in data if check_report(i) <= 1)


if __name__ == "__main__":
    inp = get_input("input")
    print(summarize_part_1(inp))
    print(summarize_part_2(inp))
