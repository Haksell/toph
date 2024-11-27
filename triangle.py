# ruff: noqa: E731, E741
from math import sqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        a, b, c = sorted(mir())
        if a + b < c:
            print("Oh, No!")
            continue
        s = (a + b + c) / 2
        res = sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"{res:.2f}")


if __name__ == "__main__":
    main()
