# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b, c, d = mir()
    print("YES" if a or b + c + d >= 2 else "NO")


if __name__ == "__main__":
    main()
