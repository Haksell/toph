# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for line in sys.stdin:
        upper = lower = digit = False
        res = 0
        for c in line:
            upper = upper or c.isupper()
            lower = lower or c.islower()
            digit = digit or c.isdigit()
            if upper and lower and digit:
                res += 1
                upper = lower = digit = False
        print(res)


if __name__ == "__main__":
    main()
