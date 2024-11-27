# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b = sorted(mir())
    print(sum(a + c > b and a + b > c for c in range(1, 200)))


if __name__ == "__main__":
    main()
