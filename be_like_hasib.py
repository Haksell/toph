# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    hi, x = mir()
    res = 0
    lo = 1
    while lo < hi:
        res += 1
        mi = lo + hi >> 1
        if x > mi:
            lo = mi + 1
        else:
            hi = mi
    print(res)


if __name__ == "__main__":
    main()
