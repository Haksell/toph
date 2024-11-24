# ruff: noqa: E731
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for i in rir():
        a, b = mir()
        print(f"Case {i+1}:", a * a + b * b)


if __name__ == "__main__":
    main()
