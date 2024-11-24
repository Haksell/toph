# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    print(float(input()) ** 2 * math.pi)


if __name__ == "__main__":
    main()
