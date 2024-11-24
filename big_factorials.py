# ruff: noqa: E731, E741
from math import factorial
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    print("0000" if n >= 20 else factorial(n) % 10000)


if __name__ == "__main__":
    main()
