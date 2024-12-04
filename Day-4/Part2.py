from get_input import get_input

def check_xmas(l: list[str]) -> int:
    ans = 0
    for i in range(len(l) - 2):
        for j in range(len(l[i]) - 2):
            a = l[i][j] + l[i + 1][j + 1] + l[i + 2][j + 2]
            b = l[i + 2][j] + l[i + 1][j + 1] + l[i][j + 2]
            if a == "MAS" or a == "SAM":
                if b == "MAS" or b == "SAM":
                    ans += 1
    return ans

if __name__ == "__main__":
    print(check_xmas(get_input("input")))