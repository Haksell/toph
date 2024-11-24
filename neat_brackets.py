# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = 0
    for c in input():
        if c == "(":
            n += 1
        elif c == ")":
            if n == 0:
                print("No")
                return
            n -= 1
    print("Yes" if n == 0 else "No")


if __name__ == "__main__":
    main()
