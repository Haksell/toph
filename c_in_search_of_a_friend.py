# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    points = [lmir() for _ in rir()]
    print(*min(points, key=lambda p: p[0] * p[0] + p[1] * p[1]))


if __name__ == "__main__":
    main()
