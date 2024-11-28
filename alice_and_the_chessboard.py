# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        x1, y1, x2, y2 = mir()
        print("Yes" if abs(x1 - x2) == abs(y1 - y2) else "No")


if __name__ == "__main__":
    main()
