import re
from get_input import get_input

def part1(inp: str) -> int:
    inp = inp.split("mul")
    ans = 0
    for i in inp:
        if re.findall("^\\(", i):
            ind = i.find(")")
            if 5 <= ind <= 9 and ',' in i:
                a = i[1:ind].split(',')
                ans += int(a[0])*int(a[1])
    return ans

if __name__ == "__main__":
    print(part1(get_input("input")))
