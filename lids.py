# ruff: noqa: E731, E741
from functools import cache
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(limit):
    if limit == 1_000_000_000:
        res = solve(limit - 1)
        res[1] += 10
        return res
    if limit <= 9:
        return [0, limit, 0, 0, 0, 0, 0, 0, 0, 0]

    @cache
    def helper(i, ss, limited):
        if i == len(digits):
            res = [0] * 10
            res[ss] = 1
            return res
        res = [0] * 10
        for d in range(digits[i] + 1 if limited else 10):
            subres = helper(i+1,ss+, d, d == digits[0])
            for i, r in enumerate(subres):
                res[i] += r
        return res

    res = [0] * 10
    digits = list(map(int, str(limit)))
    for d in range(1, digits[0] + 1):
        subres = helper(1, 1, d, d == digits[0])
        for i, r in enumerate(subres):
            res[i] += r
    return res

"""
2
111 114
15432  15432
"""

def main():
    for case in rir():
        lo, hi = mir()
        res_hi = solve(hi)
        res_lo = solve(lo - 1)
        res = list(map(int.__sub__, res_hi, res_lo))
        for i in range(9, 0, -1):
            if res[i]:
                print(f"Case {case+1}: {i} {res[i]}")
                break


if __name__ == "__main__":
    main()
