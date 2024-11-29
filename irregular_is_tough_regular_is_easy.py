# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for i in rir():
        n = ir()
        res = n * (n - 1) * (n - 2) * (n - 3) // 24
        print(f"Case {i+1}: {res}")


if __name__ == "__main__":
    main()
