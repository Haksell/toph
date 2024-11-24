# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b = mir()
    while a and b:
        a, x = divmod(a, 10)
        b, y = divmod(b, 10)
        if x + y >= 10:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
