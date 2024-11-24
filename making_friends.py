# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    i = isqrt(n)
    res = -1
    for i in range(1, i + 1):
        if n % i == 0:
            res += 1 + (i * i != n)
    print(res)


if __name__ == "__main__":
    main()
