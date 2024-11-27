# ruff: noqa: E731, E741
from math import pi
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

FRAC_TAU_8 = pi / 4


def main():
    for line in sys.stdin:
        a, *radii = map(int, line.split())
        res = a * a - sum(r * r * FRAC_TAU_8 for r in radii)
        print(f"{res:.3f}")


if __name__ == "__main__":
    main()
