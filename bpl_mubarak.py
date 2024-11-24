# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def fmt(n, word):
    if n == 0:
        return []
    elif n == 1:
        return [f"{n} {word}"]
    else:
        return [f"{n} {word}S"]


def main():
    for _ in rir():
        n = sum(c not in "DNW" for c in input())
        overs, balls = divmod(n, 6)
        print(*(fmt(overs, "OVER") + fmt(balls, "BALL")))


if __name__ == "__main__":
    main()
