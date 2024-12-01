from get_input import get_input

def count_same_numbers(l: list) -> dict:
    res = {}
    for i in l:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

def count_similarities(l: list, hashmap: dict) -> int:
    ans = 0
    for i in l:
        if i in hashmap:
            ans += i * hashmap[i]
    return ans

if __name__ == '__main__':
    print(count_similarities(get_input("input")[0], count_same_numbers(get_input("input")[1])))