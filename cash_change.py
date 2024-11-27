# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    res = []
    for value in [500, 100, 50, 10, 5, 1]:
        quantity, n = divmod(n, value)
        res.extend([value] * quantity)
    print(*reversed(res))


if __name__ == "__main__":
    main()
