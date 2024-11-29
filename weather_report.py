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
    print(
        "Bad weather."
        if n >= 70
        else "Good weather."
        if n <= 30
        else '"Confusing weather."'
    )


if __name__ == "__main__":
    main()
