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
    s = input()
    print("Change needed" if any(map(str.__eq__, s, s[1:])) else "No change needed")


if __name__ == "__main__":
    main()
