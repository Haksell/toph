# ruff: noqa: E731, E741
from math import pi
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        r, a = mir()
        print(pi * r**2 * a / 360)


if __name__ == "__main__":
    main()
