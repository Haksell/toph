# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b = input().split()
    print("BWlhaictke"[(ord(a[-1]) ^ ord(b[-1])) & 1 :: 2])


if __name__ == "__main__":
    main()