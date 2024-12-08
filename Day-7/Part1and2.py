from itertools import product
from get_input import get_input

def evaluate(numbers: list[int], operators: tuple) -> int:
    ans = numbers[0]
    for i in range(len(numbers) - 1):
        if operators[i] == "+":
            ans += numbers[i + 1]
        if operators[i] == "*":
            ans *= numbers[i + 1]
        if operators[i] == "||":
            ans = int(str(ans) + str(numbers[i + 1]))
    return ans

def check(res: int, numbers: list[int], operators: list[str]) -> int:
    operators = list(product(operators, repeat=len(numbers) - 1))
    ans = 0
    for i in operators:
        e = evaluate(numbers, i)
        if e == res:
            ans += e
            break
    return ans

def summarize(inp: list, operators: list[str]):
    ans = 0
    for i in inp:
        ans += check(i[0], i[1], operators)
    return ans

if __name__ == "__main__":
    print(summarize(get_input("input"), ["+", "*"]))
    print(summarize(get_input("input"), ["+", "*", "||"]))

