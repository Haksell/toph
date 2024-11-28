# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    SQUARED_DIGITS = [0, 1, 4, 9, 6, 5, 6, 9, 4, 1]
    for _ in rir():
        d = int(input()[-1])
        print(SQUARED_DIGITS[d])


if __name__ == "__main__":
    main()
