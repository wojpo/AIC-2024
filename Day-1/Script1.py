from get_input import get_input

def bubble_sort(l: list) -> list:
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

def summarize(l1: list, l2: list) -> int:
    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))

if __name__ == '__main__':
    print(summarize(bubble_sort(get_input("input")[0]), bubble_sort(get_input("input")[1])))

