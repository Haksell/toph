# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    goats = [input() for _ in rir()]
    goats = ["baa" if g == "ba" else g[:-1] if len(g) % 2 == 0 else g for g in goats]
    longest = max(map(len, goats))
    for goat in goats:
        print(" " * ((longest - len(goat)) // 2) + goat)


if __name__ == "__main__":
    main()
