# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    y = ir()
    print("Yes" if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else "No")


if __name__ == "__main__":
    main()
