# ruff: noqa: E731, E741
from math import sqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

FACTOR = 6 * sqrt(3) / 4


def main():
    for _ in rir():
        print(ir() ** 2 * FACTOR)


if __name__ == "__main__":
    main()
