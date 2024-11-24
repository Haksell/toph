# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    h, w = mir()
    field = [input() for _ in range(h)]
    print(
        sum(
            (
                cell != "*"
                and (y == 0 or field[y - 1][x] != "*")
                and (y == h - 1 or field[y + 1][x] != "*")
                and (x == 0 or field[y][x - 1] != "*")
                and (x == w - 1 or field[y][x + 1] != "*")
            )
            for y, row in enumerate(field)
            for x, cell in enumerate(row)
        )
    )


if __name__ == "__main__":
    main()
