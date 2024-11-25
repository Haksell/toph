# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for line in sys.stdin:
        a, b = sorted(map(int, line.split()))
        res = (a + b) * (b - a + 1) >> 1
        print(f"Sum of {a} to {b} is -> {res};")


if __name__ == "__main__":
    main()
