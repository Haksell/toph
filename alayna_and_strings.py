# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    s = input()
    print(sum(map(str.isupper, s)), sum(map(str.islower, s)))


if __name__ == "__main__":
    main()
