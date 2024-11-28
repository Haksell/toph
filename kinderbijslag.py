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
        m, p, n = mir()
        print(f"Case {i+1}:", "YES" if m * 100 >= p * n else "NO")


if __name__ == "__main__":
    main()
