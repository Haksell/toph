# ruff: noqa: E731, E741
from itertools import product
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

NEIGHBORS = list(product([-1, 0, 1], repeat=2))


def main():
    h, w = mir()
    grid = [input() for _ in range(h)]
    res = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "*":
                res.append("*")
            else:
                adjacent_mines = sum(
                    0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "*"
                    for nx, ny in product([x - 1, x, x + 1], [y - 1, y, y + 1])
                )
                res.append("." if adjacent_mines == 0 else str(adjacent_mines))
        res.append("\n")
    print("".join(res), end="")


if __name__ == "__main__":
    main()
