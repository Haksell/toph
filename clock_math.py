# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    h, m = mir()
    h = 30 * h + m / 2
    m *= 6
    print(min(abs(h - m), 360 + h - m, 360 + m - h))


if __name__ == "__main__":
    main()
