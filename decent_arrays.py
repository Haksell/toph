# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    a = lmir()
    print("Yes" if all(x <= y for x, y in zip(a, a[1:])) else "No")


if __name__ == "__main__":
    main()