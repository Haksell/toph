# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    s = input()
    counter = Counter(s)
    print(max("0123456789", key=lambda digit: counter[digit]))


if __name__ == "__main__":
    main()
