# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for i in rir():
        r = float(input())
        print(f"Case {i+1}: {1.7168*r*r:.2f}")


if __name__ == "__main__":
    main()
