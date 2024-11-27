# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

VOWELS = set("aeiou")


def main():
    for _ in rir():
        print("Yes" if VOWELS & set(input()) else "No")


if __name__ == "__main__":
    main()
