# ruff: noqa: E731, E741
from math import pi, sqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        diameter = sqrt(float(input()))
        radius = diameter / 2
        shape_area = diameter**2 - pi * radius**2
        shape_perimeter = 2 * pi * radius
        print(shape_area, shape_perimeter)


if __name__ == "__main__":
    main()
